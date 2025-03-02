from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required
from .models import Lead
from django.contrib.auth.models import User

# Create your views here.
@login_required
def dashboard(request):
    messages.success(request, "Welcome Back")
    return render(request, 'dashboard.html')

# ---------------------------------------------------------------------------------- #
# Leads Module
@login_required
def leads(request):
    leads = Lead.objects.all()
    return render(request, 'leads.html', { 'leads': leads })

# Edit Lead
@login_required
def edit_leads(request, id):
    leads = get_object_or_404(Lead, id=id)

    if request.method == 'POST':
        leads.fullname = request.POST['fullname']
        leads.email = request.POST['email']
        leads.phone = request.POST['phone']
        leads.value_property = request.POST['value_property']
        leads.mortgage = request.POST['mortgage']
        leads.state = request.POST['state']
        leads.save()
        messages.success(request, "Lead updated successfully!")
        return redirect('admin_dashboard:leads')
    else:
        messages.error(request, "Error updating lead!")
        return redirect('admin_dashboard:leads')

# Delete Lead
@login_required
def delete_leads(request, id):
    leads = get_object_or_404(Lead, id=id)
    leads.delete()
    messages.success(request, "Lead deleted successfully!")
    return redirect('admin_dashboard:leads')

# ---------------------------------------------------------------------------------- #
# Users Module
@login_required
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', { 'users': users }) 

# Register User
@login_required
def register_user(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            try:
                user = User.objects.create_user(
                username=username, 
                email=email, 
                password=password1, 
                first_name=first_name, 
                last_name=last_name,
                )
                login(request, user)
                messages.success(request, "User registered successfully!")
                return redirect('admin_dashboard:users')
            except InterruptedError:
                messages.error(request, "Error registering user!")
                return redirect('admin_dashboard:users')
        else:
            messages.error(request, "Passwords do not match!")
            return redirect('admin_dashboard:users')
    return render(request, 'users.html')

# Edit Users 
@login_required
def edit_users(request, id):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']

        user = User.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()
        messages.success(request, "User updated successfully!")
        return redirect('admin_dashboard:users')
    else:
        messages.error(request, "Error updating user!")
        return redirect('admin_dashboard:users')

# Delete Users
@login_required
def delete_users(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect('admin_dashboard:users')

# Signout Users
def signout(request):
    logout(request)
    signup_url = reverse('accounts_security:signup')
    messages.success(request, "You have successfully logged out")
    return redirect(signup_url)