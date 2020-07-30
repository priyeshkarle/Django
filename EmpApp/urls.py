from django.contrib import admin
from django.urls import path, include
from EmpApp import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('new_employee', views.new_employee, name='new_employee'),
    path('deleteall', views.deleteall, name='deletall')
]