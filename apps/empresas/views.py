from django.http.response import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from apps.empresas.models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('OK')


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']