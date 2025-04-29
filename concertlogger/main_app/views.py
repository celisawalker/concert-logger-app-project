from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .models import Concert
# Create your views here.

class Home(LoginView):
    template_name = 'home.html'