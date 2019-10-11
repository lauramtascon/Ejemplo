"""Ejemplo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from apps.mascota.views import index, mascota_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mascota/', include ('apps.mascota.urls')),
    url(r'^adopcion/', include ('apps.adopcion.urls')),
    url(r'^nuevo$', mascota_view, name='mascota_crear'),
]
