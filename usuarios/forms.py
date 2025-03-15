from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'grupo']
        widgets = {
            'grupo': forms.RadioSelect(), 
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            if field_name != 'grupo':  
                field.widget.attrs.setdefault('class', 'form-control')
        self.fields['telefone'].widget.attrs.update({'data-mask': '(00) 0000-0000'})