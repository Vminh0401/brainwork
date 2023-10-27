from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password != cpassword:
            messages.success(request, 'Sai mk')
            return render(request, '../templates/admin_register/Admin_signup.html')

        else:
            user_admin = User.objects.create_superuser(username, email, password)
            user_admin.save()
            return render(request, '../templates/admin_login/Admin_login.html')
    return render(request, '../templates/admin_register/Admin_signup.html')


def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, '../templates/admin_page/Admin_page.html')
        else:
            messages.success(request, 'Try Again!!')
            return render(request, '../templates/admin_login/Admin_login.html')
    else:
        return render(request, '../templates/admin_login/Admin_login.html')


def admin_page(request):
    return render(request, '../templates/admin_page/Admin_page.html')


def sign_out(request):
    pass
