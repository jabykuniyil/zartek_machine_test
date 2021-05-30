from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import Tags

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password, is_superuser=True)
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        messages.error(request, 'Invalid Credentials')
        return redirect(login)
    else:
        return render(request, 'admin/login.html')
    
@login_required(login_url='/login/')
def home(request):
    if request.method == 'POST':
        pass
    tags = ['models', 'vehicles', 'movies', 'technology', 'buildings', 'arts', 'science', 'sports', 'bussiness', 'animals', 'birds', 'education']
    context = {'tags' : tags}
    return render(request, 'admin/home.html', context)

@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return redirect(login)
