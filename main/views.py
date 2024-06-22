from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
# Create your views here.
def query1(req):
    #esto sirve solo una vez (viernes 21.06.2024)
    cursor = connection.cursor()
    cursor.execute("insert into main_curso (cod, nombre, activo) values('RP4','Repostería', true)")
    return HttpResponse('Listo')