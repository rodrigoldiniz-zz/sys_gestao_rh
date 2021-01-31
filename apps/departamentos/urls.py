from django.urls import path
from apps.departamentos.views import (DepartamentoList,
                                      DepartamentoCreate,
                                      DepartamentoEdit,
                                      DepartamentoDelete,
                                      )

app_name = 'departamentos'

urlpatterns = [
    path('', DepartamentoList.as_view(),
         name='list_departamentos'),
    path('novo/', DepartamentoCreate.as_view(),
         name='create_departamentos'),
    path('update/<int:pk>',
         DepartamentoEdit.as_view(),
         name='update_departamentos'),
    path('deletar/<int:pk>',
         DepartamentoDelete.as_view(),
         name='delete_departamentos')
]
