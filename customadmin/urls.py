from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('admin-page/', admin_page, name='admin_page'),

]