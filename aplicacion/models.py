from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class arbitro (models.Model):
   nombre=models.CharField(max_length=100,verbose_name='Nombre',default='Nombre por defecto')
   promedio_rojo=models.DecimalField(max_digits=5, decimal_places=2,verbose_name='Promedio de Tarjetas Rojas',default='0.0')
   promedio_amarillo=models.DecimalField(max_digits=5, decimal_places=2,verbose_name='Promedio de Tarjetas Amarillas',default='0.0')
 
   def __str__(self):
      return str(self.nombre)

class partido (models.Model):
    equipo_local= models.CharField(max_length=100,verbose_name='Equipo Local',default='Nombre por defecto')
    equipo_visitante=models.CharField(max_length=100,verbose_name='Equipo Visitante',default='Nombre por defecto')
    arbitro=models.ForeignKey(arbitro,max_length=100,verbose_name='Arbitro',on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante}"

class  preguntas (models.Model):
   autor=models.CharField(max_length=100,verbose_name='Autor',default='Nombre por defecto')
   preguntas=models.TextField(max_length=200,verbose_name='Preguntas',default='Pregunta por defecto')
  
   def __str__(self):
      return str(self.autor)  
  
class calendario (models.Model):
   lugar=models.CharField(max_length=100,verbose_name='Lugar',default='Lugar')
   fecha=models.DateField(max_length=100,verbose_name='Fecha',default='00/00/00')
   hora=models.TimeField(max_length=100,verbose_name='Hora',default='00:00')
   partido=models.ForeignKey(partido,max_length=100,verbose_name='Partido',on_delete=models.CASCADE)
   
class respuesta (models.Model):
   pregunta=models.ForeignKey(preguntas,max_length=200,verbose_name='Preguntas',on_delete=models.CASCADE)
   respuesta=models.TextField(max_length=200,verbose_name='Respuesta',default='Respuesta por defecto')
   
class resultado (models.Model):
   partido= models.ForeignKey(partido,verbose_name='Partido' ,on_delete=models.CASCADE)
   resultado=models.CharField(max_length=100,verbose_name='Resultado',default='0-0')
   ganador=models.CharField(max_length=100,verbose_name='Ganador',default='Empate')
   
class equipo (models.Model):
   equipo=models.CharField(max_length=100,verbose_name='Equipo')
   puntos=models.IntegerField(verbose_name='Puntos',default='0')
   
   
   
   @receiver(post_save, sender=resultado)
   def actualizar_puntos_equipos(sender, instance, created, **kwargs):
    if created:
        if instance.ganador.lower() == "empate":
            # Buscar y actualizar puntos para el equipo local y visitante
            equipo_local = equipo.objects.filter(equipo=instance.partido.equipo_local).first()
            equipo_visitante = equipo.objects.filter(equipo=instance.partido.equipo_visitante).first()
            if equipo_local:
                equipo_local.puntos += 1
                equipo_local.save()
            if equipo_visitante:
                equipo_visitante.puntos += 1
                equipo_visitante.save()
        else:
            # Buscar y actualizar puntos para el equipo ganador
            equipo_ganador = equipo.objects.filter(equipo=instance.ganador).first()
            if equipo_ganador:
                equipo_ganador.puntos += 3
                equipo_ganador.save()
                
                
   @receiver(post_delete, sender=resultado)
   def revertir_puntos_equipos(sender, instance, **kwargs):
    # Obtener el partido asociado al resultado eliminado
    partido = instance.partido
    
    if instance.ganador.lower() == "empate":
        # Buscar y revertir puntos para el equipo local y visitante
        equipo_local = equipo.objects.filter(equipo=partido.equipo_local).first()
        equipo_visitante = equipo.objects.filter(equipo=partido.equipo_visitante).first()
        if equipo_local:
            equipo_local.puntos -= 1
            equipo_local.save()
        if equipo_visitante:
            equipo_visitante.puntos -= 1
            equipo_visitante.save()
    else:
        # Buscar y revertir puntos para el equipo ganador
        equipo_ganador = equipo.objects.filter(equipo=instance.ganador).first()
        if equipo_ganador:
            equipo_ganador.puntos -= 3
            equipo_ganador.save()