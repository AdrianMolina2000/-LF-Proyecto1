import re

class Ruta_o:
    def __init__(self, n, p, i, f):
        self.nombre = n
        self.peso = p
        self.inicio = i
        self.fin = f

class Estacion_o:
    def __init__(self, n, e, c):
        self.nombre = n
        self.estado = e
        self.color = c

def leer_archivo(path):
    pattern1 = r"</ruta>"
    pattern2 = r"</estacion>"
    pattern3 = r">[^\s|^0-9]{1,3}<"

    with open(path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        linea = ""
        for i in lineas:
            linea += i.replace("\n", "")
            linea = linea.replace(" ", "")
            linea = re.sub(pattern3, "><", linea)
            linea = re.sub(pattern1, "</ruta> ", linea)
            linea = re.sub(pattern2, "</estacion> ", linea)
        return linea.split()


def Agrupar(ruta):
    pattern_Ruta = r"(<ruta>).*(</ruta>)"
    pattern_Estacion = r"(<estacIon>).*(</estacion>)"
    lista_rutas = []
    lista_estaciones = []
    lista_nombre = []
    lista_completa = []
    for i in ruta:
        if re.search(pattern_Ruta, i):
            lista_rutas.append(i)
        elif re.search(pattern_Estacion, i):
            lista_estaciones.append(i)
        else:
            lista_nombre.append(i)
    lista_completa.append(lista_rutas)
    lista_completa.append(lista_estaciones)
    lista_completa.append(lista_nombre)

    return lista_completa
            
def Limpiar_Ruta(ruta_entrada):
    ruta = ruta_entrada.replace("<ruta>", "")
    ruta = ruta.replace("</ruta>", "")
    pattern_nombre = r"<nombre>.*</nombre>"
    pattern_peso = r"<peso>.*</peso>"
    pattern_inicio = r"<inicio>.*</inicio>"
    pattern_fin = r"<fin>.*</fin>"
    
    #Busca el nombre
    nombre_l = re.findall(pattern_nombre, ruta)
    nombre = nombre_l[0].replace("<nombre>", "")
    nombre = nombre.replace("</nombre>", "")

    #Busca el peso
    peso_l = re.findall(pattern_peso, ruta)
    peso = peso_l[0].replace("<peso>", "")
    peso = peso.replace("</peso>", "")

    #Busca el inicio
    inicio_l = re.findall(pattern_inicio, ruta)
    inicio = inicio_l[0].replace("<inicio>", "")
    inicio = inicio.replace("</inicio>", "")

    #Busca el fin
    fin_l = re.findall(pattern_fin, ruta)
    fin = fin_l[0].replace("<fin>", "")
    fin = fin.replace("</fin>", "")

    #Crear objeto Ruta
    ruta_dev = Ruta_o(nombre, peso, inicio, fin)
    return ruta_dev



def Limpiar_Estacion(estacion_entrada):
    estacion = estacion_entrada.replace("<estacIon>", "")
    estacion = estacion.replace("</estacion>", "")
    pattern_nombre = r"<nombre>.*</nombre>"
    pattern_estado = r"<estado>.*</estado>"
    pattern_color = r"<color>.*</color>"

    #Busca el nombre
    nombre_l = re.findall(pattern_nombre, estacion)
    nombre = nombre_l[0].replace("<nombre>", "")
    nombre = nombre.replace("</nombre>", "")

    #Busca el estado
    estado_l = re.findall(pattern_estado, estacion)
    estado = estado_l[0].replace("<estado>", "")
    estado = estado.replace("</estado>", "")

    #Busca el color
    color_l = re.findall(pattern_color, estacion)
    color = color_l[0].replace("<color>", "")
    color = color.replace("</color>", "")

    #Crear objeto estacion
    estacion_dev = Estacion_o(nombre, estado, color)
    return estacion_dev

def Limpiar_Nombre(nombre_entrada):
    nombre = nombre_entrada.replace("<nombre>", "")
    nombre = nombre.replace("</nombre>", "")

    return nombre


""" 
    pattern_extra = r">(\$|@|”|"|'|[A-Za-z0-9]|\?|!|)*<"
    pattern_Ruta = r"(<ruta>).*(</ruta>)"
    pattern_Ruta_nombre = r"<nombre>.*</nombre>"
    pattern_Ruta_peso = r"<peso>.*</peso>"
    pattern_Ruta_inicio = r"<inicio>.*</inicio>"
    pattern_Ruta_fin = r"<fin>.*</fin>"
    pattern_nombre = r"[a-zA-Z]+([a-zA-Z]|[0-9]|[_]|[@]|[#])*"
    pattern_peso = r"[0-9]+(\.[0-9][0-9]*)?"
    pattern_inicio_fin = r"[a-zA-Z]+([a-zA-Z]|[0-9]|[_])*"
"""