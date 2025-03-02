from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.urls import reverse

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            username=username, 
            password=password)
        if user is None:
            messages.error(request, "Invalid username or password, try again!")
            return render(request, 'signup.html')
        else:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            dashboard_url = reverse('admin_dashboard:dashboard')
            return redirect(dashboard_url) 
    else:
        messages.error(request, "Invalid username or password")
        redirect('accounts_security:signup')
    return render(request, 'signup.html')