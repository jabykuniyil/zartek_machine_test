from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import APIView
from rest_framework import serializers
from rest_framework.response import Response
from superadmin.models import PostDetails
from .serializers import PostSerializer

# Create your views here.

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username = username, password=password, is_superuser=False)
#         if user is not None:
#             auth.login(request, user)
#             return redirect(home)
#         messages.error(request, 'Invalid Credentials')
#     else:
#         return render(request, 'user/login.html')

# @login_required(login_url='user/login/')
class Home(APIView):

    def get(self, request):
        posts = PostDetails.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(Self, request):
        pass
                