from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('tenant_dashboard/', views.tenant_dashboard, name='tenant_dashboard'),
    path('realtor_dashboard/', views.realtor_dashboard, name='realtor_dashboard'),
    path('register/', views.register, name='register'),
    path('tenant_registration/', views.tenant_registration, name='tenant_registration'),
    # path('realtor_registration/', views.realtor_registration, name='realtor_registration'),
    # path('realtor_registration_phase2/', views.realtor_registration_phase2, name='realtor_registration_phase2')
]
