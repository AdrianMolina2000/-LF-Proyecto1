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


ruta_abierta = r"[<][^/]*[r|R][u|U][t|T][a|A][.|^<]*[>]"
ruta_cerrada = r"[<][/][.|>]*[r|R][u|U][t|T][a|A][.|^<]*[>]"
nombre_abierta = r"[<][^/]*[N|n][O|o][M|m][B|b][R|r][E|e][.|^<]*[>]"
nombre_cerrada = r"[<][/][.|>]*[N|n][O|o][M|m][B|b][R|r][E|e][.|^<]*[>]"
inicio_abierta = r"[<][^/]*[I|i][N|n][I|i][C|c][I|i][O|o][.|^<]*[>]"
inicio_cerrada = r"[<][/][.|>]*[I|i][N|n][I|i][C|c][I|i][O|o][.|^<]*[>]"
fin_abierta = r"[<][^/]*[F|f][I|i][N|n][.|^<]*[>]"
fin_cerrada = r"[<][/][.|>]*[F|f][I|i][N|n][.|^<]*[>]"
peso_abierta = r"[<][^/]*[P|p][E|e][S|s][O|o][.|^<]*[>]"
peso_cerrada = r"[<][/][.|>]*[P|p][E|e][S|s][O|o][.|^<]*[>]"

estacion_abierta = r"[<][^/]*[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n][.|^<]*[>]"
estacion_cerrada = r"[<][/][.|>]*[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n][.|^<]*[>]"
estado_abierta = r"[<][^/]*[E|e][S|s][T|t][A|a][D|d][O|o][.|^<]*[>]"
estado_cerrada = r"[<][/][.|>]*[E|e][S|s][T|t][A|a][D|d][O|o][.|^<]*[>]"
color_abierta = r"[<][^/]*[C|c][O|o][L|l][O|o][R|r][.|^<]*[>]"
color_cerrada = r"[<][/][.|>]*[C|c][O|o][L|l][O|o][R|r][.|^<]*[>]"

pattern1 = r"[<][/][.|>]*[r|R][u|U][t|T][a|A][.|^<]*[>]"
pattern2 = r"[<][/][.|>]*[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n][.|^<]*[>]"
pattern3 = r">[^\s|^0-9]{1,2}<"
pattern_nombre_no = r"[^A-Za-z0-9|@|#|_|\S]"


def leer_archivo(path):

    with open(path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        linea = ""
        for i in lineas:
            linea += i.replace("\n", "")
            linea = linea.replace(" ", "")
            linea = re.sub(pattern_nombre_no, "><", linea)
            linea = re.sub(ruta_abierta, " <ruta>", linea)
            linea = re.sub(ruta_cerrada, "</ruta> ", linea)

            linea = re.sub(estacion_abierta, " <estacion>", linea)
            linea = re.sub(estacion_cerrada, "</estacion> ", linea)


        return linea.split()


def Agrupar(ruta):

    pattern_Ruta = r"[<][^/]*[r|R][u|U][t|T][a|A][\S|^<]*[>].*[<][/][.|>]*[r|R][u|U][t|T][a|A][.|^<]*[>]"
    pattern_Estacion = r"[<][^/]*[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n][\S|^<]*[>].*[<][/][.|>]*[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n][.|^<]*[>]"
    pattern_nombre = r"[<][^/]*[N|n][O|o][M|m][B|b][R|r][E|e][\S|^<]*[>].*[<][/][.|>]*[N|n][O|o][M|m][B|b][R|r][E|e][.|^<]*[>]"
    
    lista_rutas = []
    lista_estaciones = []
    lista_nombre = []
    lista_completa = []
    for i in ruta:
        if re.search(pattern_Ruta, i):
            lista_rutas.append(i)
        elif re.search(pattern_Estacion, i):
            lista_estaciones.append(i)
        elif re.search(pattern_nombre,i):
            lista_nombre.append(i)
        else:
            continue
    lista_completa.append(lista_rutas)
    lista_completa.append(lista_estaciones)
    lista_completa.append(lista_nombre)

    return lista_completa


def Limpiar_Ruta(ruta_entrada):

    ruta = re.sub(ruta_abierta, "", ruta_entrada)
    ruta = re.sub(ruta_cerrada, "", ruta)


    pattern_nombre = r"[<][^/]*[N|n][O|o][M|m][B|b][R|r][E|e][.|^<]*[>].*[<][/][.|>]*[N|n][O|o][M|m][B|b][R|r][E|e][.|^<]*[>]"
    pattern_peso = r"[<][^/]*[P|p][E|e][S|s][O|o][.|^<]*[>].*[<][/][.|>]*[P|p][E|e][S|s][O|o][.|^<]*[>]"
    pattern_inicio = r"[<][^/]*[I|i][N|n][I|i][C|c][I|i][O|o][.|^<]*[>].*[<][/][.|>]*[I|i][N|n][I|i][C|c][I|i][O|o][.|^<]*[>]"
    pattern_fin = r"[<][^/]*[F|f][I|i][N|n][.|^<]*[>].*[<][/][.|>]*[F|f][I|i][N|n][.|^<]*[>]"

    # Busca el nombre
    nombre_l = re.findall(pattern_nombre, ruta)
    nombre = re.sub(nombre_abierta, "", nombre_l[0])
    nombre = re.sub(nombre_cerrada, "", nombre)

    # Busca el peso
    peso_l = re.findall(pattern_peso, ruta)
    peso = re.sub(peso_abierta, "", peso_l[0])
    peso = re.sub(peso_cerrada, "", peso)

    # Busca el inicio
    inicio_l = re.findall(pattern_inicio, ruta)
    inicio = re.sub(inicio_abierta, "", inicio_l[0])
    inicio = re.sub(inicio_cerrada, "", inicio)

    # Busca el fin
    fin_l = re.findall(pattern_fin, ruta)
    fin = re.sub(fin_abierta, "", fin_l[0])
    fin = re.sub(fin_cerrada, "", fin)

    # Crear objeto Ruta
    ruta_dev = Ruta_o(nombre, peso, inicio, fin)
    return ruta_dev


def Limpiar_Estacion(estacion_entrada):
    estacion = re.sub(estacion_abierta, "", estacion_entrada)
    estacion = re.sub(estacion_cerrada, "", estacion)

    pattern_nombre = r"[<][^/]*[N|n][O|o][M|m][B|b][R|r][E|e][.|^<]*[>].*[<][/][.|>]*[N|n][O|o][M|m][B|b][R|r][E|e][.|^<]*[>]"
    pattern_estado = r"[<][^/]*[E|e][S|s][T|t][A|a][D|d][O|o][.|^<]*[>].*[<][/][.|>]*[E|e][S|s][T|t][A|a][D|d][O|o][.|^<]*[>]"
    pattern_color = r"[<][^/]*[C|c][O|o][L|l][O|o][R|r][.|^<]*[>].*[<][/][.|>]*[C|c][O|o][L|l][O|o][R|r][.|^<]*[>]"

    # Busca el nombre

    nombre_l = re.findall(pattern_nombre, estacion)
    nombre = re.sub(nombre_abierta, "", nombre_l[0])
    nombre = re.sub(nombre_cerrada, "", nombre)

    # Busca el estado
    estado_l = re.findall(pattern_estado, estacion)
    estado = re.sub(estado_abierta, "", estado_l[0])
    estado = re.sub(estado_cerrada, "", estado)

    # Busca el color
    color_l = re.findall(pattern_color, estacion)
    color = re.sub(color_abierta, "", color_l[0])
    color = re.sub(color_cerrada, "", color)

    # Crear objeto estacion
    estacion_dev = Estacion_o(nombre, estado, color)
    return estacion_dev


def Limpiar_Nombre(nombre_entrada):
    nombre = re.sub(nombre_abierta, "", nombre_entrada)
    nombre = re.sub(nombre_cerrada, "", nombre)

    return nombre


print(Agrupar(leer_archivo("input2.txt"))[0])
# lista_texto = leer_archivo("input1.txt")
# lista_etiquetas = Agrupar(lista_texto)
# Rutas = []
# Estaciones = []
# # Rutas
# for i in lista_etiquetas[0]:
#     Rutas.append(Limpiar_Ruta(i))
# # Estaciones
# for i in lista_etiquetas[1]:
#     Estaciones.append(Limpiar_Estacion(i))
# # Nombre
# nombre = Limpiar_Nombre(lista_etiquetas[2][0])


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
"<estacion><estado>disponible</estado><color>#f5f5f5</color><nombre>FUEGO</nombre></estacion>"
"""