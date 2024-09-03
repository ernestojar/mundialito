from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',index,name='index'),
    path('login/', views.login, name='login'),
    path('nosotros', nosotros, name='nosotros'),
    #path('logout/', SignedOutView.as_view(), name='logout'),
    path('desloguear/', views.desloguear,name='desloguear'),
    
    # Gestionar Partidos
    path('Listar_Partidos/', views.Listar_Partidos, name='Listar_Partidos'),
    path('Crear_Partidos/', views.Crear_Partidos, name='Crear_Partidos'),
    path('Modificar_Partidos/<id>/', views.Modificar_Partidos, name='Modificar_Partidos'),
    path('Eliminar_Partidos/<id>/', views.Eliminar_Partidos, name='Eliminar_Partidos'),
    
    
    # Gestionar Arbitros
    path('Listar_Arbitros', views.Listar_Arbitros, name='Listar_Arbitros'),
    path('Crear_Arbitros/', views.Crear_Arbitros, name='Crear_Arbitros'),
    path('Modificar_Arbitros/<id>/', views.Modificar_Arbitros, name='Modificar_Arbitros'),
    path('Eliminar_Arbitros/<id>/', views.Eliminar_Arbitros, name='Eliminar_Arbitros'),
    
   
   #Gestionar preguntas
   path('Listar_Preguntas', views.Listar_Preguntas, name='Listar_Preguntas'),
   path('Crear_Preguntas/', views.Crear_Preguntas, name='Crear_Preguntas'),
   path('Eliminar_Preguntas/<id>/', views.Eliminar_Preguntas, name='Eliminar_Preguntas'),
   
   
   #Gestionar respuestas
   path('Crear_Respuestas/', views.Crear_Respuestas, name='Crear_Respuestas'),
   path('Eliminar_Respuestas/<id>/', views.Eliminar_Respuestas, name='Eliminar_Respuestas'),
   
   #Resultado
   path('Listar_Resultados',views.Listar_Resultados,name='Listar_Resultados'),
   path('Crear_Resultados/',views.Crear_Resultados, name='Crear_Resultados'),
   path('Modificar_Resultados/<id>/',views.Modificar_Resultados, name='Modificar_Resultados'),
   path('Eliminar_Resultados/<id>/',views.Eliminar_Resultados, name='Eliminar_Resultados'),
   
   
   #Calendario
   path('Listar_Calendario',views.Listar_Calendario,name='Listar_Calendario'),
   path('Crear_Calendario/',views.Crear_Calendario, name='Crear_Calendario'),
   path('Modificar_Calendario/<id>/',views.Modificar_Calendario, name='Modificar_Calendario'),
   path('Eliminar_Calendario/<id>/',views.Eliminar_Calendario, name='Eliminar_Calendario'),
   
   
   #posiciones
    path('Listar_Posiciones',views.Listar_Posiciones,name='Listar_Posiciones'),
    
     path('Crear_Equipo/',views.Crear_Equipo, name='Crear_Equipo'),
     
     
     
     path('Eliminar_Equipo/<id>/',views.Eliminar_Equipo, name='Eliminar_Equipo'),
   
]
