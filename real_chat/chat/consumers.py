from channels.generic.websocket import AsyncWebsocketConsumer


class ChatCosumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def disconnect(self):
        pass

    async def recieve(self,text_data):
        print(text_data)