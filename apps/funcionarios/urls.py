from django.urls import path
from apps.funcionarios.views import (FuncionarioList,
                                     FuncionarioEdit,
                                     FuncionarioDelete,
                                     FuncionarioCreate)


app_name = 'funcionarios'


urlpatterns = [
    path('',
         FuncionarioList.as_view(),
         name='list_funcionarios'),
    path('editar/<int:pk>',
         FuncionarioEdit.as_view(),
         name='update_funcionarios'),
    path('deletar/<int:pk>',
         FuncionarioDelete.as_view(),
         name='delete_funcionarios'),
    path('novo/',
         FuncionarioCreate.as_view(),
         name='create_funcionarios'),
]
