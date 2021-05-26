from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password, is_superuser=True)
        if user is not None:
            return redirect(home)
        messages.error(request, 'Invalid Credentials')
    else:
        return render('admin/login.html')
    
@login_required(login_url='/login/')
def home(request):
    return render(request, 'admin/home.html')
