from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, curso


class BoostrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class']= 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=40, required=True, label='Nombre')
    last_name = forms.CharField(max_length=40, required=True, label='Apellido')

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        def __int__(self, *args, **kwargs):
            super.__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].wiget.attrs.update({'class': 'form-control'})
                self.fields['username'].label = 'Nombre de usuario'
                self.fields['password1'].label = 'Contraseña'
                self.fields['password2'].label = 'Confirmar contraseña'

class CursoForm(BoostrapFormMixin, forms.ModelForm):
    class Meta:
        model = curso
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'cupos', 'estado']

        widgets = {
            'fecha_inicio': forms.DateInput(attrib={'type':'date'}),
            'fecha_fin':  forms.DateInput(attrib={'type': 'date'}),
        }