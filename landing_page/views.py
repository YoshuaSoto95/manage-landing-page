from django.db import IntegrityError
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from .models import Lead
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#Landing Page vista
def index(request):
    return render(request, 'index.html')

#Thankyou Page de Landing
def thankyou_page(request):
    return render(request, 'thankyou_page.html')

# Dashboard
@login_required
def dashboard(request):
    return render(request, 'base.html')

# Mostrar los Leads

@login_required
def leads(request):
    leads = Lead.objects.all()
    return render(request, 'leads.html', {'leads': leads})

# Capturar Lead
def registrar_lead(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        valor_propiedad = request.POST['valor_propiedad']
        monto = request.POST['monto']
        estado = request.POST['estado']

        if nombre and email and telefono and valor_propiedad and monto and estado:
            Lead.objects.create(
                nombre=nombre,
                email=email,
                telefono=telefono,
                valor_propiedad=valor_propiedad,
                monto=monto,
                estado=estado
            )
            return redirect('landing_page:thankyou_page')
    return render(request, 'index.html')

# Editar Lead Formulario
@login_required
def editar_lead(request, id):
    lead = get_object_or_404(Lead, id=id)
    if request.method == 'POST':
        lead.nombre = request.POST['nombre']
        lead.email = request.POST['email']
        lead.telefono = request.POST['telefono']
        lead.valor_propiedad = request.POST['valor_propiedad']
        lead.monto = request.POST['monto']
        lead.estado = request.POST['estado']
        lead.save()
        return redirect('landing_page:leads')
    return render(request, 'editar_lead.html', {'lead': lead})

#Eliminar los Leads
@login_required
def eliminar_leads(request, id):
    lead = get_object_or_404(Lead, id=id)
    lead.delete()
    return redirect('landing_page:leads')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'El usuario no existe')
            return redirect('landing_page:signin')
        else:
            login(request, user)
            messages.error(request, 'Te has logueado correctamente')
            return redirect('landing_page:dashboard')
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
    
        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request, user)
                messages.error(request, 'Te has registrado correctamente')
                return redirect('landing_page:dashboard')
            except:
                messages.error(request, 'El usuario ya existe')
                return redirect('landing_page:signup')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('landing_page:signup')
    return render(request, 'signup.html')

def signout(request):
    logout(request)
    messages.error(request, 'Te has deslogueado correctamente')
    return redirect('landing_page:signin')

@login_required
def users(request):
    users =  User.objects.all()
    return render(request, 'users.html', {'users': users})