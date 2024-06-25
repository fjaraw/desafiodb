from django.shortcuts import render, redirect
# Create your views here.
def counter(req):
    #consultar si ya existe la variable
    veces = req.session.get('veces', None)
    #si accede por primera vez, variable se inicaliza en 0
    if veces is None:
        veces = 0
    #agregar 1 a la cantidad de visitas del usuario
    veces += 1
    #guardar valor en sesion
    req.session['veces'] = veces
    return render(req, 'counter.html')

def reset_counter(req):
    req.session['veces']=0
    return redirect('/counter')