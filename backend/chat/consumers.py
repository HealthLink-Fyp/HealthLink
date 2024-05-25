import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Chat
from core.models import DoctorProfile, PatientProfile
from channels.exceptions import StopConsumer


class ChatConsumer(WebsocketConsumer):
    connected_users = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = None
        self.room_group_name = None
        self.user = None
        self.doctor = None
        self.patient = None

    def is_authenticated(self, user):
        """
        Check if the user is authenticated.
        """

        return user and hasattr(user, "is_authenticated") and user.is_authenticated

    def send_group_message(self, event_type, user, message, profile=None):
        """
        Send a message to the group.
        """

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": event_type,
                "user": user,
                "profile": profile,
                "message": message,
            },
        )

    def chat_room_create(self, doctor_id: int, patient_id: int):
        """
        Create a chat room.
        """

        self.room_name = f"chat_{doctor_id}_{patient_id}"
        self.room_group_name = f"grp_{self.room_name}"

        self.chat_room = (
            Chat.objects.filter(room_name=self.room_name).order_by("-created").first()
        )

        if not self.chat_room:
            self.chat_room = Chat.objects.create(room_name=self.room_name)

    def connect(self):
        """
        Called when the websocket is handshaking as part of the connection process.
        """
        self.user = self.scope.get("user")

        role = self.user.role

        self.accept()

        # Check if the user is authenticated
        if not self.is_authenticated(self.user):
            self.close(code=4001, reason="User is not authenticated.")
            return

        # Check if one doctor and one patient are connected
        if ChatConsumer.connected_users >= 2 and self.user.role == "patient":
            self.close(code=4001, reason="Chat room is full.")
            return

        if role == "doctor":
            doctor_id = self.user.id
            patient_id = self.scope["url_route"]["kwargs"]["user_id"]
            self.chat_room_create(doctor_id=doctor_id, patient_id=patient_id)
            self.chat_room.doctor = self.user.doctor
            print("\npatient_id: ", patient_id)
            self.chat_room.patient = PatientProfile.objects.get(user__id=patient_id)

        elif role == "patient":
            doctor_id = self.scope["url_route"]["kwargs"]["user_id"]
            patient_id = self.user.id
            self.chat_room_create(doctor_id=doctor_id, patient_id=patient_id)
            self.chat_room.patient = self.user.patient
            print("\npatient_id: ", doctor_id)
            self.chat_room.doctor = DoctorProfile.objects.get(user__id=doctor_id)

        self.chat_room.save()

        ChatConsumer.connected_users += 1

        # Add the user to the group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.notify_user_join()

    def disconnect(self, code):
        """
        Called when the WebSocket closes for any reason.
        """

        if self.is_authenticated(self.user):
            # Remove the user from the group
            async_to_sync(self.channel_layer.group_discard)(
                self.room_group_name, self.channel_name
            )

            self.notify_user_leave()

            ChatConsumer.connected_users -= 1

            raise StopConsumer()

        raise StopConsumer()

    def receive(self, text_data):
        """
        Called when a message is received from the WebSocket.
        """

        try:
            if isinstance(text_data, str):
                message = text_data
            else:
                json_text = json.loads(text_data)
                message = json_text.get("message", "")

            if (
                not self.user
                or not hasattr(self.user, "is_authenticated")
                or not self.user.is_authenticated
            ):
                message = f"Anonymous: {message}"

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": f"{str(self.user).capitalize()}: {message}"
                },
            )

            # Save the message to the database
            if message:
                Chat.objects.create(
                    room_name=self.room_name,
                    doctor=self.chat_room.doctor,
                    patient=self.chat_room.patient,
                    message=message,
                )

        except Exception as e:
            print(f"An error occurred: {e}")

    def chat_message(self, event):
        """
        Called when a message is received from the group.
        """

        try:
            self.send(text_data=json.dumps(event))
        except Exception as e:
            print(f"An error occurred: {e}")

    def notify_user_join(self):
        """
        Notify the users in the group when a user joins the chat room.
        """

        join_message = {
            "type": "chat_message",
            "message": f"{str(self.user.role.capitalize())} {str(self.user.username).capitalize()}, has joined the chat room.",
        }
        self.send(text_data=json.dumps(join_message))

    def notify_user_leave(self):
        """
        Notify the users in the group when a user leaves the chat room.
        """

        leave_message = {
            "type": "chat_message",
            "message": f"{str(self.user.role.capitalize())} {str(self.user.username).capitalize()}, has left the chat room.",
        }
        self.send(text_data=json.dumps(leave_message))
