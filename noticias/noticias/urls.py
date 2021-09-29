"""noticias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from sitio import views


urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('ejemplo_form_pelado/', views.ejemplo_form_pelado),
    path('ejemplo_form_django/', views.ejemplo_form_django),
    path('api/cantidades/', views.cantidades),
    path('api/cantidades/html/', views.cantidades_html),
    path('robots.txt', views.robots_txt),
    path('search/', include('haystack.urls')),
    path('admin/', admin.site.urls),
]
