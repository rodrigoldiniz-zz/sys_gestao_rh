from django.urls import path
from apps.funcionarios.views import home


app_name = 'funcionarios'


urlpatterns = [
    path('', home),
]
