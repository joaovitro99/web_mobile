from django.shortcuts import render
from django.urls import reverse_lazy
from veiculo.models import Veiculo
from veiculo.forms import FormularioVeiculo
from django.views.generic import ListView,CreateView,View,UpdateView,DeleteView
from django.http import FileResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView,DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from veiculo.serializers import SerializadorVeiculo
# Create your views here.
class ListarVeiculos(LoginRequiredMixin, ListView):
    model = Veiculo 
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_html'] = 'base.html' 
        return context
    
class CriarVeiculos(CreateView):
    model = Veiculo 
    template_name = 'veiculo/novo.html'
    form_class = FormularioVeiculo
    success_url = reverse_lazy('listar-veiculos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_html'] = 'base.html' 
        return context
    
class EditarVeiculos(LoginRequiredMixin, UpdateView):
    model = Veiculo 
    template_name = 'veiculo/editar.html'
    form_class = FormularioVeiculo
    success_url = reverse_lazy('listar-veiculos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_html'] = 'base.html' 
        return context
    
class DeletarVeiculos(LoginRequiredMixin, DeleteView):
    model = Veiculo 
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy('listar-veiculos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_html'] = 'base.html' 
        return context
    
class FotoVeiculo(View):
    def get(self,request,arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não autorizado")
        except Exception as exception:
            raise exception

class APIListarVeiculos(ListAPIView):
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()
    
class APIDeletarVeiculos(DestroyAPIView):
    serializer_class = SerializadorVeiculo 
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Veiculo.objects.all()
