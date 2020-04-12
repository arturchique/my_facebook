from django.urls import path, include, re_path
from . import views
from django.contrib.auth import login

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/logout/', views.LogoutView.as_view(), name="logout"),
    path('accounts/register/', views.RegisterView.as_view(), name="register"),
    path('accounts/profile/', views.ProfileView.as_view(), name="profile"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/', views.test, name='test')
]
