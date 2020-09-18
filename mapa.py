from graphviz import Digraph

def esta_abierta(lista_est, estacion):
    for i in lista_est:
        if i.nombre == estacion:
            if i.estado == 'cerrada':
                return False

    return True

def indice(lista_rut, buscar):
    iteracion = 0
    for i in lista_rut:
        if i.nombre == buscar:
            return iteracion
        else:
            iteracion += 1
    return iteracion


def es_mayor(lista_rut, ruta_comparacion, lista_esta2):
    bandera = False
    for i in lista_rut:
        if esta_abierta(lista_esta2, i.fin):
            if i.inicio == ruta_comparacion.inicio and float(ruta_comparacion.peso) > float(i.peso):
                return True
    return bandera


def graficar_mapa(lista):
    #Listas
    nombre = lista[2]
    lista_rutas = lista[0]
    lista_estaciones = lista[1]

    #Graficar
    t = Digraph('Mapa', filename='Mapa.gv', format="png", directory="Images/")
    
    for i in lista_estaciones:
        t.attr('node', shape='oval', fixedsize='true', width="2",  height= "1", color="black",style= "filled", fillcolor=i.color)
        t.node(i.nombre, label=i.nombre+'\n'+i.estado)

    for i in lista_rutas:

        if esta_abierta(lista_estaciones, i.inicio):
            if esta_abierta(lista_estaciones, i.fin):
                if es_mayor(lista_rutas, i, lista_estaciones):
                    t.edge(tail_name=i.inicio, head_name=i.fin, style="dashed", label=i.nombre + '\n' + i.peso)

                else:
                    t.edge(tail_name=i.inicio, head_name=i.fin, style = "bold", label=i.nombre + '\n' + i.peso)

            else: 
                t.edge(tail_name=i.inicio, head_name=i.fin, style="dashed", label=i.nombre + '\n' + i.peso)
        else: 
            t.edge(tail_name=i.inicio, head_name=i.fin, style="dashed", label=i.nombre + '\n' + i.peso)

    #penwidth = "5"
    t.attr(overlap='false')
    t.attr(label= nombre)
    t.attr(fontsize='20')

    t.view()



def graficar_ruta(lista):
    #Listas
    nombre = lista[2]
    lista_rutas = lista[0]
    lista_estaciones = lista[1]

    #Graficar
    t = Digraph('Ruta', filename='Ruta.gv', format="png", directory="Images/")
    
    for i in lista_estaciones:
        t.attr('node', shape='oval', fixedsize='true', width="2",  height= "1", color="black",style= "filled", fillcolor=i.color)
        t.node(i.nombre, label=i.nombre+'\n'+i.estado)

    for i in lista_rutas:

        if esta_abierta(lista_estaciones, i.inicio):
            if esta_abierta(lista_estaciones, i.fin):
                if es_mayor(lista_rutas, i, lista_estaciones) == False:
                    t.edge(tail_name=i.inicio, head_name=i.fin, style = "bold", label=i.nombre + '\n' + i.peso)
                    
    #penwidth = "5"
    t.attr(overlap='false')
    t.attr(label= nombre)
    t.attr(fontsize='20')
    t.attr(rankdir="LR")

    t.view()




def graficar_ruta2(lista):
    #Listas
    nombre = lista[2]
    lista_rutas = lista[0]
    lista_estaciones = lista[1]

    #Graficar
    t = Digraph('Ruta2', filename='Ruta2.gv', format="png", directory="Images/")
    t.attr('node', shape='oval', fixedsize='true', width="2",  height= "1", color="black",style= "filled", fillcolor="gray")

    for i in lista_rutas:

        if esta_abierta(lista_estaciones, i.inicio):
            if esta_abierta(lista_estaciones, i.fin):
                if es_mayor(lista_rutas, i, lista_estaciones) == False:
                    t.edge(tail_name=i.inicio, head_name=i.fin, style = "bold", label=i.nombre + '\n' + i.peso)
                    
    #penwidth = "5"
    t.attr(overlap='false')
    t.attr(label= nombre)
    t.attr(fontsize='20')
    t.attr(rankdir="LR")

    t.view()