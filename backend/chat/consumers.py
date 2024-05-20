import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer


class ChatConsumer(WebsocketConsumer):
    connected_users = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = None
        self.room_group_name = None
        self.user = None

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

    def connect(self):
        """
        Called when the websocket is handshaking as part of the connection process.
        """

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope.get("user")

        self.accept()

        # Check if the user is authenticated
        if not self.is_authenticated(self.user):
            self.close(code=4001, reason="User is not authenticated.")
            return

        # Check if one doctor and one patient are connected
        if ChatConsumer.connected_users >= 2 and self.user.role == "patient":
            self.close(code=4001, reason="Chat room is full.")
            return

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
                    "user": getattr(self.user, "username", "Anonymous"),
                    "message": message,
                },
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
            "user": self.user.username,
            "profile": self.user.role,
            "message": f"{self.user.username} has joined the chat room.",
        }
        self.send(text_data=json.dumps(join_message))

    def notify_user_leave(self):
        """
        Notify the users in the group when a user leaves the chat room.
        """

        leave_message = {
            "type": "chat_message",
            "user": self.user.username,
            "profile": self.user.role,
            "message": f"{self.user.username} has left the chat room.",
        }
        self.send(text_data=json.dumps(leave_message))
