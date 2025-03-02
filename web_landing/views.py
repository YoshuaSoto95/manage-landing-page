from django.contrib import messages
from django.shortcuts import redirect, render
from admin_dashboard.models import Lead

# Create your views here.
def index(request):
    return render(request, 'index.html')

def thankyou_page(request):
    return render(request, 'thankyou_page.html')

def register_lead(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        value_property = request.POST['value_property']
        mortgage = request.POST['mortgage']
        state = request.POST['state']

        if fullname and email and phone and value_property and mortgage and state:
            Lead.objects.create(
                fullname=fullname,
                email=email,
                phone=phone,
                value_property=value_property,
                mortgage=mortgage,
                state=state,
            )
            return redirect('web_landing:thankyou_page')
    return render(request, 'register_lead.html')