from django.shortcuts import render
from django.urls import reverse_lazy
from anuncio.models import Anuncio
from anuncio.forms import FormularioAnuncio
from django.views.generic import ListView,CreateView,View,UpdateView,DeleteView
from django.http import FileResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class ListarAnuncios(LoginRequiredMixin, ListView):
    model = Anuncio 
    context_object_name = 'anuncios'
    template_name = 'anuncio/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_html'] = 'base.html' 
        return context
    
class CriarAnuncios(CreateView):
    model = Anuncio 
    template_name = 'anuncio/novo.html'
    form_class = FormularioAnuncio
    success_url = reverse_lazy('listar-anuncios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_html'] = 'base.html' 
        return context
    
class EditarAnuncios(LoginRequiredMixin, UpdateView):
    model = Anuncio 
    template_name = 'anuncio/editar.html'
    form_class = FormularioAnuncio
    success_url = reverse_lazy('listar-anuncios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_html'] = 'base.html' 
        return context
    
class DeletarAnuncios(LoginRequiredMixin, DeleteView):
    model = Anuncio 
    template_name = 'anuncio/deletar.html'
    success_url = reverse_lazy('listar-anuncios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_html'] = 'base.html' 
        return context

# Create your views here.
