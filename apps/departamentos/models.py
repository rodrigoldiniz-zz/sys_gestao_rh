from django.urls import reverse
from django.db import models
from apps.empresas.models import Empresa


class Departamento(models.Model):
    nome = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('departamentos:list_departamentos')

    def __str__(self):
        return self.nome
