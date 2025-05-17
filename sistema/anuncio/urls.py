from django.urls import path
from anuncio.views import *

urlpatterns= [
    path('',ListarAnuncios.as_view(),name='listar-anuncios'),
    path('novo/',CriarAnuncios.as_view(),name='criar-anuncios'),
    #path('fotos/<str:arquivo>/',FotoVeiculo.as_view(),name='foto-veiculos'),
    path('deletar/<int:pk>/',DeletarAnuncios.as_view(),name='deletar-anuncios'),
    path('<int:pk>/',EditarAnuncios.as_view(),name='editar-anuncios'),
    
]