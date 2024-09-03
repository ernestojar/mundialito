from django.forms import *
from django import forms
from .models import *
from django.core.validators import RegexValidator
from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone



resultado_validator = RegexValidator(
    regex=r'^\d+-\d+$',
    message="El formato debe ser un número entero, un guion y otro número entero."
)







class Arbitro_Form(forms.ModelForm):
    error_messages = {
        'empty_field': 'Campos Vacios',
        'incorrect_field': 'Campos Incorrectos',
        'max': 'Se ha llegado al maximo de capacidad',
    }
    

   
    
    class Meta:
        model = arbitro
        fields = {
            'nombre': 'Nombre',
            'promedio_rojo': 'Promedio de Tarjetas Rojas por Partido',
            'promedio_amarillo': 'Promedio de Tarjetas Amarillas por Partido',
           }
        
        
        
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    
                    'placeholder': ''
                }
            ),
            'promedio_rojo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    
                    'placeholder': ''
                }
            ),
            'promedio_amarillo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': ''
                }
            ),}
        




class Partido_Form(forms.ModelForm):
    
    equipo_local = forms.ChoiceField(
        choices=[
           ('Facultad 1', 'Facultad 1'),
           ('Facultad 2', 'Facultad 2'),
           ('Facultad 3', 'Facultad 3'),
           ('Facultad 4', 'Facultad 4'),
           ('CITED', 'CITED'),
           ('FTE', 'FTE'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    equipo_visitante = forms.ChoiceField(
        choices=[
           ('Facultad 1', 'Facultad 1'),
           ('Facultad 2', 'Facultad 2'),
           ('Facultad 3', 'Facultad 3'),
           ('Facultad 4', 'Facultad 4'),
           ('CITED', 'CITED'),
           ('FTE', 'FTE'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    
    
   
    
    
    arbitro = forms.ModelChoiceField(
        queryset=arbitro.objects.all(), 
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': ''
        })
    )
    
    
    class Meta:
        model = partido
        fields = {
            'equipo_local': 'Equipo local',
            'equipo_visitante': 'Equipo visitante',
            
            'arbitro': 'Arbitro',
        }
    
   
    widgets = {
           
           
            'resultado': forms.TextInput(
                
                attrs={
                    'class': 'form-control',
                    'placeholder': ''
                }
            ),
            
            'arbitro': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': ''
                }
            ),
            
             'equipo_local': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': ''
                }
            ),
              'equipo_visitante': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': ''
                }
            ),
            
            }
   
        
   

    def clean(self):
        cleaned_data = super().clean()
        el = cleaned_data.get('equipo_local')
        ev = cleaned_data.get('equipo_visitante')

        # Verificar si el nombre y el apellido son iguales
        if el == ev:
            raise ValidationError(" Los Equipos local y visitante no pueden ser iguales.")

        return cleaned_data

        
        
    
        
        
        
class Preguntas_Form(forms.ModelForm):
    error_messages = {
        'empty_field': 'Campos Vacios',
        'incorrect_field': 'Campos Incorrectos',
        'max': 'Se ha llegado al maximo de capacidad',
    }
    

   
    
    class Meta:
        model = preguntas
        fields = {
            'autor': 'Autor',
            'preguntas': 'Pregunta',
            
           }
        
        
        
        widgets = {
            'autor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    
                    'placeholder': ''
                }
            ),
            'preguntas': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    
                    'placeholder': ''
                }
            ),
           }
        


class Respuestas_Form(forms.ModelForm):
    error_messages = {
        'empty_field': 'Campos Vacios',
        'incorrect_field': 'Campos Incorrectos',
        'max': 'Se ha llegado al maximo de capacidad',
    }
    

   
    
    class Meta:
        model = respuesta
        fields = {
            'pregunta': 'Pregunta',
            'respuesta': 'Respuesta',
            
           }
        
        
        
        widgets = {
            'pregunta': forms.Select(
                attrs={
                    'class': 'form-control',
                    
                    'placeholder': ''
                }
            ),
            'respuesta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    
                    'placeholder': ''
                }
            ),
           }
        
        
        
        
        

class Resultados_Form(forms.ModelForm):
    resultado = forms.CharField(validators=[resultado_validator])
    error_messages = {
        'empty_field': 'Campos Vacios',
        'incorrect_field': 'Campos Incorrectos',
        'max': 'Se ha llegado al maximo de capacidad',
    }
    ganador = forms.ChoiceField(
        choices=[
           ('Facultad 1', 'Facultad 1'),
           ('Facultad 2', 'Facultad 2'),
           ('Facultad 3', 'Facultad 3'),
           ('Facultad 4', 'Facultad 4'),
           ('CITED', 'CITED'),
           ('FTE', 'FTE'),
           ('Empate', 'Empate'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

   
    
    class Meta:
        model = resultado
        fields = {
            'partido': 'Partido',
            'resultado': 'resultado',
            'ganador': 'Ganador',
           }
        
        
        
        widgets = {
            'partido': forms.Select(
                attrs={
                    'class': 'form-control',
                    
                    'placeholder': ''
                }
            ),
            'resultado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    
                    'placeholder': ''
                }
            ),
            'Ganador': forms.Select(
                attrs={
                    'class': 'form-control',
                    
                    'placeholder': ''
                }
            ),
           }
        
    def clean_ganador(self):
        ganador = self.cleaned_data.get('ganador')
        partido = self.cleaned_data.get('partido')

        if ganador not in [partido.equipo_local, partido.equipo_visitante, 'Empate']:
            raise forms.ValidationError("Seleccione un equipo válido.")

        return ganador
     
     
    def clean(self):
        cleaned_data = super().clean()
        resultado = cleaned_data.get('resultado')
        ganador = cleaned_data.get('ganador')

        # Verificar si el resultado es un empate
        if resultado:
            partes = resultado.split('-')
            if len(partes) == 2 and partes[0] == partes[1]:
                if ganador != 'Empate':
                    self.add_error('ganador', 'Para un empate, el ganador debe ser "Empate".')
            else:
                if ganador == 'Empate':
                    self.add_error('ganador', 'No se puede seleccionar "Empate" si el resultado no es un empate.')

        return cleaned_data    


class Respuestas_Form(forms.ModelForm):
    error_messages = {
        'empty_field': 'Campos Vacios',
        'incorrect_field': 'Campos Incorrectos',
        'max': 'Se ha llegado al maximo de capacidad',
    }
    

   
    
    class Meta:
        model = respuesta
        fields = {
            'pregunta': 'Pregunta',
            'respuesta': 'Respuesta',
            
           }
        
        
        
        widgets = {
            'pregunta': forms.Select(
                attrs={
                    'class': 'form-control',
                    
                    'placeholder': ''
                }
            ),
            'respuesta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    
                    'placeholder': ''
                }
            ),
           }
        
        
        
        
        

class Calendario_Form(forms.ModelForm):
    error_messages = {
        'empty_field': 'Campos Vacios',
        'incorrect_field': 'Campos Incorrectos',
        'max': 'Se ha llegado al maximo de capacidad',
    }
    
    lugar = forms.ChoiceField(
        choices=[
           (' Cancha Futbol Sala 1', 'Cancha Futbol Sala 1'),
           (' Cancha Futbol Sala 2', 'Cancha Futbol Sala 2'),
           (' Cancha Futbol Sala 3', 'Cancha Futbol Sala 3'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    fecha=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = calendario
        fields = ['partido', 'lugar', 'fecha', 'hora']
        widgets = {
            'partido': forms.Select(attrs={'class': 'form-control'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': AdminDateWidget(attrs={'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(Calendario_Form, self).__init__(*args, **kwargs)
        # Establecer el rango mínimo de fecha a la fecha actual
        self.fields['fecha'].widget.attrs['min'] =timezone.localtime(timezone.now()).date().isoformat()

        


class Equipo_Form(forms.ModelForm):
    
    
    equipo = forms.ChoiceField(
        choices=[
           ('Facultad 1', 'Facultad 1'),
           ('Facultad 2', 'Facultad 2'),
           ('Facultad 3', 'Facultad 3'),
           ('Facultad 4', 'Facultad 4'),
           ('CITED', 'CITED'),
           ('FTE', 'FTE'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = equipo
        fields = {
            'equipo': 'Equipo',
            'puntos': 'Puntos',
            
           }
        
        
        
        widgets = {
            'equipos': forms.Select(
                attrs={
                    'class': 'form-control',
                    
                    'placeholder': ''
                }
            ),
            'puntos': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    
                    'placeholder': ''
                }
            ),
           }
        
        
        
        
        
