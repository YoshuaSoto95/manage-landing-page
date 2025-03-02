from django.urls import path
from . import views

app_name = 'accounts_security'

urlpatterns = [
    path('', views.signup, name='signup'),
]