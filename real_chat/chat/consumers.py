from channels.generic.websocket import AsyncWebsocketConsumer


class ChatCosumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name= "Chat1"


        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )


    async def recieve(self,text_data):
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_message",
                "message": text_data 
            }
        )

    async def chat_message(self,event):

        await self.send(
            text_data=event["message"]
        )