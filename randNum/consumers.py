# chat/consumers.py
import json
import redis
import threading
from random import randint
from time import sleep

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


redis_instance = redis.StrictRedis(host="127.0.0.1",
                                   port=6379, db=0)

flag = False
rn = 0


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.num_group_name = "num"

        global flag
        if not flag:
            t1 = threading.Thread(target=self.receive, daemon=True)
            t1.start()
            flag = True

        async_to_sync(self.channel_layer.group_add)(
            self.num_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.num_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self):
        while True:
            sleep(5)
            async_to_sync(self.channel_layer.group_send)(
                self.num_group_name, {"type": "rand_num"}
            )


    def rand_num(self, event):

        # Send message to WebSocket
        rn = redis_instance.get('number').decode()
        self.send(text_data=rn)
