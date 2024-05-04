import json
from channels.generic.websocket import WebsocketConsumer
from .models import Message, CustomUser
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        receiver_id = text_data_json['receiver_id']
        sender = self.scope['user']
        receiver = CustomUser.objects.get(id=receiver_id)
        new_message = Message.objects.create(sender=sender, receiver=receiver, message=message)
        
        # Send latest messages to the receiver
        messages = self.get_latest_messages(sender, receiver)
        self.send_messages_to_receiver(messages)

    def get_latest_messages(self, sender, receiver):
        sent_messages = Message.objects.filter(sender=sender, receiver=receiver)
        received_messages = Message.objects.filter(sender=receiver, receiver=sender)
        messages = sent_messages.union(received_messages).order_by('timestamp')
        return messages

    def send_messages_to_receiver(self, messages):
        message_data = [{
            'sender': message.sender.username,
            'message': message.message,
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        } for message in messages]
        self.send(text_data=json.dumps({
            'type': 'messages',
            'messages': message_data
        }))
