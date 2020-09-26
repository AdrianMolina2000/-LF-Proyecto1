import re, os
from otros import *
from analizador import analizar_archivo
from tokens import analizar_archivo_tokens
from Errores import analizar_archivo_error

def carga_archivo():
    ruta = input("Ingrese la ruta del archivo: ")
    if os.path.exists(ruta): 
        if re.search("\.txt", ruta):
            print("==========================================\n\n")
            analizar_archivo(ruta)
            analizar_archivo_tokens(ruta)
            analizar_archivo_error(ruta)
            lista_texto = leer_archivo()
            lista_etiquetas = Agrupar(lista_texto)
            Rutas = []
            Estaciones = []
            #Rutas
            
            for i in lista_etiquetas[0]:
                Rutas.append(Limpiar_Ruta(i))
            #Estaciones
            for i in lista_etiquetas[1]:
                Estaciones.append(Limpiar_Estacion(i))
            #Nombre
            nombre = Limpiar_Nombre(lista_etiquetas[2][0])
            
            lista_limpia = [Rutas, Estaciones, nombre]
            var = input("Ingrese Enter para continuar: ")
            print("Regresando a menu principal...")
            return lista_limpia
        else:
            print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("////Error -> Unicamente archivos .txt ////")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

    else:
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("/////  Error -> Ruta no encontrada  /////")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
