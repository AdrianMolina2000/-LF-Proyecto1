import re

def analizar_archivo(path):

    estado = "nada"

    with open(path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        n_linea = 1
        for linea in lineas:
            n_letra = 0
            for letra in linea:
                n_letra += 1
                if estado == "nada":
                    if letra == " ":
                        continue
                    elif letra == "<":
                        estado = "<"
                    else:
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        estado = "nada"
                elif estado == "<":
                    if letra == " ":
                        continue
                    elif letra == "R" or letra == "r":
                        estado = "<r"
                elif estado == "<r":
                    if letra == "u" or letra == "U":
                        estado = "<ru"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "<ru":
                    if letra == "T" or letra == "t":
                        estado = "<rut"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<rut":
                    if letra == "a" or letra == "A":
                        estado = "<ruta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<ruta":
                    if letra == ">":
                        estado = "<ruta>"
                    elif letra == " ":
                        estado = "<ruta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<ruta>":
                    if letra == "\n":
                        estado = "ruta_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "ruta_apertura":
                    if letra == "<":
                        estado = "r<"
                    elif letra == " ":
                        continue
                    else:
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "r<":
                    if letra == "n" or letra == "N":
                        estado = "<n"
                    elif letra == "\n":
                        continue
                    else:
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<n":
                    if letra == "o" or letra == "O":
                        estado = "<no"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<no":
                    if letra == "m" or letra == "M":
                        estado = "<nom"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<nom":
                    if letra == "b" or letra == "B":
                        estado = "<nomb"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<nomb":
                    if letra == "r" or letra == "R":
                        estado = "<nombr"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<nombr":
                    if letra == "e" or letra == "E":
                        estado = "<nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<nombre":
                    if letra == ">":
                        estado = "<nombre>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<nombre>":
                    if letra == "\n":
                        estado = "nombre_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
            n_linea += 1
                
                
            
analizar_archivo("das.txt")