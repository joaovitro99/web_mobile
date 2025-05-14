from django import forms
from .models import Veiculo  
from veiculo.consts import *

class FormularioVeiculo(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo', 'ano', 'cor', 'combustivel','foto']
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'cor': forms.Select(attrs={'class': 'form-control'}),
            'combustivel': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['marca'].choices = OPCOES_MARCAS
        self.fields['cor'].choices = OPCOES_CORES
        self.fields['combustivel'].choices = OPCOES_COMBUSTIVEL

