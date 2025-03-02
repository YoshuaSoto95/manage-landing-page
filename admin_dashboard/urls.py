from django.urls import path
from admin_dashboard import views
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Lead
    path('leads/', views.leads, name='leads'),
    path('leads/edit_leads/<int:id>', views.edit_leads, name="edit_leads"),
    path('leads/delete_leads/<int:id>', views.delete_leads, name="delete_leads"),

    # Users
    path('users/', views.users, name='users'),
    path('users/register_user/', views.register_user, name='register_user'),
    path('users/edit_user/<int:id>', views.edit_users, name="edit_user"),
    path('users/delete_user/<int:id>', views.delete_users, name="delete_users"),

    # Logout
    path('users/signout/', views.signout, name='signout'),
]
