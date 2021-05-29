from django.urls import path
from .views import *

urlpatterns = [
    # path('login/', views.login, name = 'login'),
    path('home/', Home.as_view(), name='home'),
]