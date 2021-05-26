from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password=password, is_superuser=False)
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        messages.error(request, 'Invalid Credentials')
    else:
        return render(request, 'user/login.html')

@login_required(login_url='user/login/')
def home(request):
    return render(request, 'user/home.html')
            