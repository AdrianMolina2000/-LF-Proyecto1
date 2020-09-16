from graphviz import Digraph

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
        t.edge(tail_name=i.inicio, head_name=i.fin, label=i.nombre)

    #penwidth = "5"
    t.attr(overlap='false')
    t.attr(label= nombre)
    t.attr(fontsize='20')

    t.view()