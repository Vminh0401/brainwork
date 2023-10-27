from django.contrib import admin
from django.urls import path, include
from customadmin import views
app_name = 'custom_admin'

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('sign_up/', views.sign_up, name='sign_up'),

]