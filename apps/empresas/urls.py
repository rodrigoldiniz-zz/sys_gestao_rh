from django.urls import path
from apps.empresas.views import EmpresaCreate, EmpresaEdit


app_name = 'empresas'


urlpatterns = [
    path('novo', EmpresaCreate.as_view(), name='create_empresa'),
    path('editar/<int:pk>',
         EmpresaEdit.as_view(), name='edit_empresa'),
]
