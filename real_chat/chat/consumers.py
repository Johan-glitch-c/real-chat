from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

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


    async def receive(self,text_data):
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


# from channels.generic.websocket import AsyncWebsocketConsumer


# class ChatConsumer(AsyncWebsocketConsumer):

#     async def connect(self):
#         self.group_name = "Chat1"

#         print("CONNECT:", self.channel_name)

#         await self.channel_layer.group_add(
#             self.group_name,
#             self.channel_name
#         )

#         print("ADDED TO GROUP:", self.group_name)

#         await self.accept()

#     async def disconnect(self, close_code):

#         print("DISCONNECT:", self.channel_name)

#         await self.channel_layer.group_discard(
#             self.group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):

#         print("MESSAGE:", text_data)

#         await self.channel_layer.group_send(
#             self.group_name,
#             {
#                 "type": "chat_message",
#                 "message": text_data
#             }
#         )

#         print("GROUP SEND DONE")

#     async def chat_message(self, event):

#         print(
#             "CHAT MESSAGE TO:",
#             self.channel_name,
#             event["message"]
#         )

#         await self.send(
#             text_data=event["message"]
#         )