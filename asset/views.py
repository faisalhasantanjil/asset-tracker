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
            return redirect('home')
        else:
            return redirect('signin')

    return render(request, 'asset/signin.html')