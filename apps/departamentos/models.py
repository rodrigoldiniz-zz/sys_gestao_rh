from django.db import models


class Departamento(models.Model):
    Nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
