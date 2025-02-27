from django.urls import path
from landing_page import views

app_name = 'landing_page'

urlpatterns = [

    # Landing Page
    path('', views.index, name='index'),
    path('thankyou_page/', views.thankyou_page, name='thankyou_page'),

    # Dashboard Views Protected
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/leads', views.leads, name='leads'),
    path('dashboard/leads/registrar', views.registrar_lead, name='registrar_lead'),
    path('dashboard/leads/editar/<int:id>', views.editar_lead, name='editar_lead'),
    path('dashboard/leads/eliminar/<int:id>', views.eliminar_leads, name='eliminar_leads'),

    # Login Management
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),

    # User Management Views Protected
    path('users/', views.users, name='users'),
    path('users/delete/<int:id>', views.delete_user, name='delete_user'),
]