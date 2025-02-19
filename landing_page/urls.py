from django.urls import path
from landing_page import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/leads', views.leads, name='leads'),
]