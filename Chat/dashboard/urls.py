from django.urls import path
from .views import *


urlpatterns = [
    path('', home,name='home'),
    path('chat/', chat_message,name='chat'),

]