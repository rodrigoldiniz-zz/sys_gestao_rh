from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',
         include('apps.core.urls', namespace='core')),
    path('funcionarios/',
         include('apps.funcionarios.urls', namespace='funcionarios')),
    path('empresas/',
         include('apps.empresas.urls', namespace='empresas')),
    path('admin/', admin.site.urls),
    path('accounts/',
         include('django.contrib.auth.urls')),
]
