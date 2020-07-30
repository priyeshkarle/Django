from django.shortcuts import render, redirect
from EmpApp.models import Employee
from django.db import models



# Create your views here.

def employee_list(request):
    allEmployee = Employee.objects.all()
    return render(request, 'EmpApp/employeelist.html', {'AllEmp': allEmployee})


def new_employee(request):
    if request.method == 'POST':
        first_name = request.POST['FIRSTNAME']
        last_name = request.POST['LASTNAME']

        e = Employee.objects.create()
        e.first_name = first_name
        e.last_name = last_name
        e.save()
        return redirect('employee_list')

    return render(request, 'EmpApp/newemployee.html', {})


def deleteall(request):
    Employee.objects.all().delete()
    return redirect('employee_list')