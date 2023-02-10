from argparse import Action
from email import message
import json
from channels.generic.websocket import WebsocketConsumer
from django.forms import SelectDateWidget
from .models import Post, DetailedUser


activeUsers = {}


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        activeUsers[self.scope["user"].username] = self
        self.accept()
    
    def disconnect(self, code):
        del activeUsers[self.scope["user"].username]
    
    def receive(self, text_data=None):
        data = json.loads(text_data)
        to_chat = data.get("to_send")
        message = str(data.get("message"))

        self.storeChatToDB(to_chat, message)

        if to_chat in activeUsers:
            data = {
                "message": message,
                "sender": self.scope["user"].username
            }
            activeUsers[to_chat].send(json.dumps(data))

    def storeChatToDB(self, to_chat, message):
        self = DetailedUser.objects.get(username=self.scope["user"])
        friend = DetailedUser.objects.get(username=to_chat)

        if not (message and to_chat):
            return 
        
        self_friends = json.loads(self.friends)
        for _friend in self_friends:
            if to_chat == _friend["username"]:
                break
        else:
            return 
        
        all_chats = json.loads(self.chats)
        chats = all_chats.get(to_chat)
        if not chats:
            all_chats[to_chat] = []

        
        all_chats[to_chat].append([message, 0])
        self.chats = json.dumps(all_chats)
        self.save()

        friend_all_chats = json.loads(friend.chats)

        chats = friend_all_chats.get(self.username)
        if not chats:
            friend_all_chats[self.username] = []
        
        friend_all_chats[self.username].append([message, 1])
        friend.chats = json.dumps(friend_all_chats)
        friend.save()
