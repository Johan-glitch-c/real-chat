from django.db import models
from users.models import Users
# Create your models here.



class Chat(models.Model):

    users = models.ManyToManyField(Users)


class Message(models.Model):

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField(null = True, blank = True)
    img = models.ImageField(null = True, blank = True,upload_to = "user_images/")
    author = models.ForeignKey(Users,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"