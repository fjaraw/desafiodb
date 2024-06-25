from django.db import models

# Create your models here.
class Tarea(models.Model):
    descripcion = models.TextField(default='', unique=True)
    eliminada = models.BooleanField(default=False)
    # subtareas = [SubTarea 1, SubTarea 2, ...]

class SubTarea(models.Model):
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, related_name='subtareas', on_delete=models.CASCADE)

'''
Ej uso related_name:

st5 = Subtarea.objects.get(5)
st5.tarea.descripcion

t2 = tarea.objects.get(2)
for sub_tarea in t2.subtareas:
    print(f'Una de las subtareas es {sub_tarea.descripcion}')
'''