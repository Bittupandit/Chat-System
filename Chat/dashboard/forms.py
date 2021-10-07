from django import forms
from django.db.models import fields
from .models import *

class ChatForm(forms.ModelForm):
    class Meta:
        model = ChatModel
        fields = ['message'] 