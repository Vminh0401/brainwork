from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('admin_page/', admin_page, name='admin_page'),
    path('sign_up/', admin_register, name='sign_up'),

]