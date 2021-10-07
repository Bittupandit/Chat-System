from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
from django.contrib.auth import get_user_model


class ChatModel(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}"