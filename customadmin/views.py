from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def admin_login(request):
    return render(request, '../templates/admin_login/Admin_login.html')
