from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms  import  *
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate

from django.http import HttpRequest
from django.views.generic.base import TemplateView

# Create your views here.

def index (request):
    return render(request,"index.html")

def login (request):
    return render(request,"Registration/login.html")

def nosotros (request):
    return render(request,"nosotros.html")

def Calendario (request):
    return render(request,"calendario.html")

#def partidos (request):
   # return render(request,"partidos.html")

def posiciones (request):
    return render(request,"posiciones.html")

def Preguntas (request):
    return render(request,"preguntas.html")

#def arbitros (request):
    #return render(request,"arbitros.html")


#arbitros

def Listar_Arbitros(request):
    lista =arbitro.objects.all()
    return render(request, 'Arbitros/arbitros.html', {'lista': lista})


@login_required
def Crear_Arbitros(request):
    if request.POST:
        formulario = Arbitro_Form (request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Listar_Arbitros')
        else:
            return render(request, 'Arbitros/crear_arbitros.html', {'formulario': formulario})

    formulario = Arbitro_Form ()
    return render(request, 'Arbitros/crear_arbitros.html', {'formulario': formulario})

@login_required
def Modificar_Arbitros(request, id):
    Arbitro = arbitro.objects.get(id=id)
    formulario =  Arbitro_Form (request.POST or None, request.FILES or None, instance=Arbitro)
    if formulario.is_valid():
        formulario.save()
        return redirect('Listar_Arbitros')
    return render(request, 'Arbitros/modificar_arbitros.html', {'formulario': formulario})

@login_required
def Eliminar_Arbitros(request, id):
    wawa = get_object_or_404(arbitro, id=id)
    wawa.delete()
    return redirect('Listar_Arbitros')





#partido

def Listar_Partidos(request):
    lista = partido.objects.all()
    return render(request, 'Partido/partidos.html', {'lista': lista})

@login_required
def Crear_Partidos(request):
    if request.POST:
        formulario = Partido_Form (request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Listar_Partidos')
        else:
            return render(request, 'Partido/crear_partido.html', {'formulario': formulario})

    formulario = Partido_Form ()
    return render(request, 'Partido/crear_partido.html', {'formulario': formulario})


@login_required
def Modificar_Partidos(request, id):
    Partido = partido.objects.get(id=id)
    formulario =  Partido_Form (request.POST or None, request.FILES or None, instance=Partido)
    if formulario.is_valid():
        formulario.save()
        return redirect('Listar_Partidos')
    return render(request, 'Partido/modificar_partido.html', {'formulario': formulario})

@login_required
def Eliminar_Partidos(request, id):
    p = get_object_or_404(partido, id=id)
    p.delete()
    return redirect('Listar_Partidos')


#preguntas

def Listar_Preguntas(request):
    pregunt = preguntas.objects.all()
    return render(request, 'Preguntas/preguntas.html', {'preguntas': pregunt,})


@login_required
def Crear_Preguntas(request):
    if request.POST:
        formulario = Preguntas_Form (request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Listar_Preguntas')
        else:
            return render(request, 'Preguntas/crear_preguntas.html', {'formulario': formulario})

    formulario = Preguntas_Form ()
    return render(request, 'Preguntas/crear_preguntas.html', {'formulario': formulario})


@login_required
def Eliminar_Preguntas(request, id):
    p = get_object_or_404(preguntas, id=id)
    p.delete()
    return redirect('Listar_Preguntas')


#respuestas

@login_required
def Crear_Respuestas(request):
    if request.POST:
        formulario = Respuestas_Form (request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Listar_Preguntas')
        else:
            return render(request, 'Preguntas/crear_respuestas.html', {'formulario': formulario})

    formulario = Respuestas_Form ()
    return render(request, 'Preguntas/crear_respuestas.html', {'formulario': formulario})


@login_required
def Eliminar_Respuestas(request, id):
    p = get_object_or_404(respuesta, id=id)
    p.delete()
    return redirect('Listar_Preguntas')





#Resultados

def Listar_Resultados(request):
    lista_resultados=resultado.objects.all()
    return render(request,"Resultado/resultado.html", {"lista" :lista_resultados})


@login_required
def Crear_Resultados(request):
    if request.POST:
        formulario = Resultados_Form (request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Listar_Resultados')
        else:
            return render(request, 'Resultado/crear_resultado.html', {'formulario': formulario})

    formulario = Resultados_Form ()
    return render(request, 'Resultado/crear_resultado.html', {'formulario': formulario})




@login_required
def Modificar_Resultados(request, id):
    res = resultado.objects.get(id=id)
    formulario =  Resultados_Form (request.POST or None, request.FILES or None, instance=res)
    if formulario.is_valid():
        formulario.save()
        return redirect('Listar_Resultados')
    return render(request, 'Resultado/modificar_resultado.html', {'formulario': formulario})

@login_required
def Eliminar_Resultados(request, id):
    p = get_object_or_404(resultado, id=id)
    p.delete()
    return redirect('Listar_Resultados')



#Calendario


def Listar_Calendario(request):
    lista=calendario.objects.all().order_by('fecha')
    return render(request,"Calendario/calendario.html", {"lista" : lista})


@login_required
def Crear_Calendario(request):
    if request.POST:
        formulario = Calendario_Form (request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Listar_Calendario')
        else:
            return render(request, 'Calendario/crear_calendario.html', {'formulario': formulario})

    formulario = Calendario_Form ()
    return render(request, 'Calendario/crear_calendario.html', {'formulario': formulario})




@login_required
def Modificar_Calendario(request, id):
    c = calendario.objects.get(id=id)
    formulario =  Calendario_Form (request.POST or None, request.FILES or None, instance=c)
    if formulario.is_valid():
        formulario.save()
        return redirect('Listar_Calendario')
    return render(request, 'Calendario/modificar_calendario.html', {'formulario': formulario})

@login_required
def Eliminar_Calendario(request, id):
    p = get_object_or_404(calendario, id=id)
    p.delete()
    return redirect('Listar_Calendario')

  
  
  #posiciones
  
def Listar_Posiciones(request):
    lista=equipo.objects.all().order_by('-puntos')
    return render(request,"posiciones.html", {"lista" : lista})


#equipo
@login_required
def Crear_Equipo(request):
    if request.POST:
        formulario = Equipo_Form (request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Listar_Posiciones')
        else:
            return render(request, 'Equipo/equipo.html', {'formulario': formulario})

    formulario = Equipo_Form ()
    return render(request,  'Equipo/equipo.html', {'formulario': formulario})



@login_required
def Eliminar_Equipo(request, id):
    p = get_object_or_404(equipo, id=id)
    p.delete()
    return redirect('Listar_Posiciones')
 
 #deslogear

#class SignedOutView(TemplateView):
    #template_name = "registration/signed_out.html"

    #def get(self, request: HttpRequest):
       # logout(request)
       # return render(request, self.template_name)

def desloguear(request):
    logout (request)
    return redirect('/')