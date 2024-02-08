from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import time
from django.shortcuts import get_object_or_404

from django.conf import settings
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    form_a = UserForm()
    form_b = CompanyForm()
    if request.method == 'POST':
        form_a = UserForm(request.POST)
        form_b = CompanyForm(request.POST)
        form_a.instance.username = request.POST['email']
        if form_a.is_valid() and form_a.is_valid():
            login(request, form_a.save())
            form_b.instance.user = request.user
            form_b.save()
            return redirect('signin')
    context = {
        'form_a': form_a,
        'form_b': form_b
    }
    return render(request, 'asset/signup.html', context)

# Login to system
def signin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tempo')
        else:
            return redirect('signin')

    return render(request, 'asset/signin.html')

#user login or not checking
#@login_required(login_url='signin')
def tempo(request):
    user= request.user
    context = {
        'user': user
    }
    return render(request, 'asset/temp.html')

# Logout
def signout(request):
    logout(request)
    return redirect('signin')

def addemployee(request):
    form = EmployeeForm()
    #form.fields['start_date'].widget = DateTimePickerInput()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        form.instance.company = CompanyInformation.objects.get(
            user=request.user.id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

    context = {
        'form': form,
    }
    return render(request, 'asset/addemployee.html', context)


def employeelist(request):
    company = CompanyInformation.objects.get(user=request.user.id)
    employees = EmployeeInformation.objects.filter(company=company.id)

    context = {
        'employees': employees
    }
    return render(request, 'asset/viewEmployee.html', context)

def employeedetails(request, pk):
    company = CompanyInformation.objects.get(user=request.user.id)
    employee = get_object_or_404(EmployeeInformation,id=pk,company=company)
    assets = AssetTrack.objects.filter(
        employee=employee.id)
    
    context = {
        'employee': employee,
        'assets': assets,
    }

    return render(request, 'asset/employeeDetails.html', context)

def assign_asset(request):
    company = CompanyInformation.objects.get(user=request.user.id)
    employees = EmployeeInformation.objects.filter(company=company.id)
    
    form = AssetAssignForm()
    #form.fields['start_date'].widget = DateTimePickerInput()
    if request.method == 'POST':
        form = AssetAssignForm(request.POST)
        request.POST['email']
        form.instance.company = CompanyInformation.objects.get(
            user=request.user.id)
        form.instance.employee = request.POST['employee']
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

    context = {
        'form': form,
        'employees': employees,
    }
    return render(request, 'asset/assignAsset.html', context)