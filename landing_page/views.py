from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Lead

# Create your views here.

#Landing Page vista
def index(request):
    return render(request, 'index.html')

#Thankyou Page de Landing
def thankyou_page(request):
    return render(request, 'thankyou_page.html')

# Dashboard
def dashboard(request):
    return render(request, 'base.html')

# Mostrar los Leads
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
def eliminar_leads(request, id):
    lead = get_object_or_404(Lead, id=id)
    lead.delete()
    return redirect('landing_page:leads')