"""
URL configuration for KeyServ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.profesional.views import HomeView
from django.contrib.auth import views as aunth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('apps.cliente.urls')),
    path('profesionales/', include('apps.profesional.urls')),
    path("login/", aunth_views.LoginView.as_view(),name='login'),
    path("logout/", aunth_views.LogoutView.as_view()),

    #para agregar el home al arrancar el servidor
    path('', HomeView.as_view(), name='home'),
]
