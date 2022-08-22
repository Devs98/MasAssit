"""MasAssist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('quienes-somos/', views.quienessomos, name='quienes-somos'),
    path('quienes-ser-proovedor/', views.proveedor, name='proovedor'),
    path('reembolsos/', views.reembolsos, name='reembolsos'),
    path('pqrs/', views.pqrs, name='pqrs'),
    path('contacto/', views.contacto, name='contacto'),
    path('blog/', views.blog, name='blog'),
    path('newsletter/', views.Newsletter, name='newsletter'),
    path('eutanasia/', views.eutanasia, name='eutanasia'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
