from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('tenant_dashboard/', views.TenantDashboardView.as_view(), name='tenant_dashboard'),
    path('realtor_dashboard/', views.RealtorDashboardView.as_view(), name='realtor_dashboard'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('tenant_registration/', views.TenantRegistrationView.as_view(), name='tenant_registration'),
    path('realtor_registration/', views.RealtorRegistrationView.as_view(), name='realtor_registration'),
    path('realtor_registration_phase2/', views.RealtorRegistrationPhase2View.as_view(), name='realtor_registration_phase2'),
    path('create',views.CreateListingView.as_view(),name= 'create'),
    path('update/<int:pk>',views.UpdateListingView.as_view(),name= 'update'),
    path('delete/<int:pk>', views.DeleteListingView.as_view(), name='delete'),
    path('profileupdate/<int:pk>',views.UpdateProfileView.as_view(),name='profile_update')
]
