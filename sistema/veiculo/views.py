from django.shortcuts import render
from veiculo.models import Veiculo
from django.views.generic import ListView
# Create your views here.
class ListarVeiculos(ListView):
    model = Veiculo 
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_html'] = 'base.html' 
        return context
