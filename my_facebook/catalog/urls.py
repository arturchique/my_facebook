from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]
