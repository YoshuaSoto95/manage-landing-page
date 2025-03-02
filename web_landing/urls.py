from django.urls import path
from . import views

app_name = 'web_landing'

urlpatterns = [
    path('', views.index, name='index'),
    path('register_lead/', views.register_lead, name='register_lead'),
    path('thankyou_page/', views.thankyou_page, name='thankyou_page'),
]
