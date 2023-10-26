from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def admin_login(request):
    return render(request, '../templates/admin_login/Admin_login.html')


def admin_register(request):
    return render(request, '../templates/admin_register/Admin_signup.html')


def admin_page(request):
    return render(request, '../templates/admin_page/Admin_page.html')
