import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = None
        self.room_group_name = None
        self.user = None

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope["user"]

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_add)(
                f"user_{self.user.id}", self.channel_name
            )

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        if isinstance(text_data, str):
            message = text_data
        else:
            json_text = json.loads(text_data)
            message = json_text["message"]

        if not self.user.is_authenticated:
            message = f"Anonymous: {message}"

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {"type": "chat_message", "user": self.user.username, "message": message},
        )

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))

    def user_join(self, event):
        self.send(text_data=json.dumps(event))

    def user_leave(self, event):
        self.send(text_data=json.dumps(event))
