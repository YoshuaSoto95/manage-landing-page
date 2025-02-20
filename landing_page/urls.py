from django.urls import path
from landing_page import views

app_name = 'landing_page'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/leads', views.leads, name='leads'),
    path('dashboard/leads/registrar', views.registrar_lead, name='registrar_lead'),
    path('dashboard/leads/editar/<int:id>', views.editar_lead, name='editar_lead'),
    path('dashboard/leads/eliminar/<int:id>', views.eliminar_leads, name='eliminar_leads'),

    path('thankyou_page/', views.thankyou_page, name='thankyou_page'),
]