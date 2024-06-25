from dia3.models import Tarea, SubTarea

def crear_nueva_tarea(*descripciones: str):
    #multiples tareas: crear_nueva_tarea('t1', 't2', 't3')
    for descripcion in descripciones:
        t = Tarea(descripcion = descripcion)
        t.save()
    imprimir_en_pantalla()

def crear_subtarea(idTarea:int, *descripciones: str):
    t = Tarea.objects.get(id=idTarea)
    #multiples subtareas: crear_subtarea(idTarea, 't1', 't2', 't3')
    for descripcion in descripciones:
        st = SubTarea(descripcion = descripcion, tarea = t)
        st.save()

def elimina_tarea(idTarea:int):
    t = Tarea.objects.get(id=idTarea)
    t.eliminada = True
    t.save()

def elimina_sub_tarea(idSubTarea:int):
    st = SubTarea.objects.get(id=idSubTarea)
    st.eliminada = True
    st.save()

def recuperar_tareas_y_subtareas():
    tareas = Tarea.objects.filter(eliminada=False)
    return tareas

def imprimir_en_pantalla():
    tareas = recuperar_tareas_y_subtareas()
    for t in tareas:
        print (f'[{t.id}] {t.descripcion}')
        if t.subtareas:
            for st in t.subtareas.filter(eliminada=False):
                print (f'   [{st.id}] {st.descripcion}')