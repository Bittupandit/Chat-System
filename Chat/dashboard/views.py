from django.shortcuts import redirect, render,HttpResponse
from account.models import *
from .forms import *
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


def home(request):
    users = User.objects.all().exclude(is_superuser=True)
    for u in users:
        print(u.email)
    messages = ChatModel.objects.all()
    # messages_u = ChatModel.objects.all().exclude(sender=request.user)

    context = {'users':users,'messages':messages}
    return render(request,'dashboard/home.html',context)

def chat_message(request):
    if request.method == "POST":
        message = request.POST.get('message')
        chat = ChatModel.objects.create(sender=request.user,message=message)
        chat.save()
    return redirect('home')