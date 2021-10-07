from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate, logout
# Create your views here.
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('home')
        else:
            print(form.errors)
    context = {'form':form}
    return render(request,'account/registration.html',context)

def logout_request(request):
    logout(request)
    return redirect('home')


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)

                return redirect('home')
            else:
                pass
        else:
            print(form.errors)
            
    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request,'account/login.html',context)