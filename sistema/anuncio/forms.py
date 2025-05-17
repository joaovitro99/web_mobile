from django import forms
from .models import Anuncio, Veiculo  # Importe seus modelos

class FormularioAnuncio(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['titulo', 'descricao', 'diaria', 'disponivel', 'veiculo'] 
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}), 
            'diaria': forms.NumberInput(attrs={'class': 'form-control'}), 
            'disponivel': forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            'veiculo': forms.Select(attrs={'class': 'form-control'}), 
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['veiculo'].queryset = Veiculo.objects.all()
        