import re

def analizar_archivo(path):

    estado = "nada"
    pattern_primera_Letra = r"[A-Za-z]"
    pattern_nombre = r"[A-Za-z0-9|@|#|_]"
    pattern_nombre_no = r"[^A-Za-z0-9|@|#|_|\s]"

    
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
                    elif letra == "\n":
                        continue
                    else:
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        
                elif estado == "<":
                    if letra == " ":
                        continue
                    #RUTA
                    elif letra == "R" or letra == "r":
                        estado = "<r"
                    
                    #Estacion
                    elif letra == "e" or letra == "E":
                        estado = "<e"
                #RUTA
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
                    elif letra == "\n":
                        continue
                    else:
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "r<":
                    #nombre
                    if letra == "n" or letra == "N":
                        estado = "r<n"

                    #peso
                    elif letra == "p" or letra == "P":
                        estado = "r<p"

                    #inicio
                    elif letra == "i" or letra == "I":
                        estado = "r<i"
                    
                    #fin
                    elif letra == "f" or letra == "F":
                        estado = "r<f"
                    
                    #rutaCierre
                    elif letra == "/":
                        estado = "r</"

                    elif letra == "\n":
                        continue

                    else:
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                #Estacion
                elif estado == "<e":
                    if letra == "s" or letra == "S":
                        estado = "<es"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "<es":
                    if letra == "T" or letra == "t":
                        estado = "<est"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<est":
                    if letra == "a" or letra == "A":
                        estado = "<esta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<esta":
                    if letra == "c" or letra == "C":
                        estado = "<estac"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<estc":
                    if letra == "i" or letra == "I":
                        estado = "<estaci"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<estaci":
                    if letra == "o" or letra == "O":
                        estado = "<estacio"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<estcio":
                    if letra == "n" or letra == "N":
                        estado = "<estacion"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")

                elif estado == "<estacion":
                    if letra == ">":
                        estado = "<estacion>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "<estacion>":
                    if letra == "\n":
                        estado = "estacion_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "estacion_apertura":
                    if letra == "<":
                        estado = "e<"
                    elif letra == " ":
                        continue
                    elif letra == "\n":
                        continue
                    else:
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "e<":
                    #nombre
                    if letra == "n" or letra == "N":
                        estado = "e<n"

                    #estado
                    elif letra == "e" or letra == "E":
                        estado = "e<e"

                    #color
                    elif letra == "c" or letra == "C":
                        estado = "e<i"
                    
                    #estacionCierre
                    elif letra == "/":
                        estado = "e</"
                    
                    elif letra == "\n":
                        continue

                    else:
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")

                #Estacion
                elif estado == "e<n":
                    if letra == "o" or letra == "O":
                        estado = "e<no"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<no":
                    if letra == "m" or letra == "M":
                        estado = "e<nom"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<nom":
                    if letra == "b" or letra == "B":
                        estado = "e<nomb"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<nomb":
                    if letra == "r" or letra == "R":
                        estado = "e<nombr"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<nombr":
                    if letra == "e" or letra == "E":
                        estado = "e<nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<nombre":
                    if letra == ">":
                        estado = "e<nombre>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<nombre>":
                    if letra == "\n":
                        estado = "e_nombre_primera_letra"
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "estacion_nombre"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e_nombre_primera_letra":
                    if letra == " ":
                        continue
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "estacion_nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "estacion_nombre":
                    if re.search(pattern_nombre, letra) :
                        continue
                    elif letra == " ":
                        continue
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "estacion_nombreCierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "estacion_nombreCierre":
                    if letra == "/" :
                        estado = "estacion_nombreCierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "estacion_nombreCierre/":
                    if letra == "n" or letra =="N" :
                        estado = "e</n"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</n":
                    if letra == "o" or letra == "O" :
                        estado = "e</no"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</no":
                    if letra == "m" or letra == "M" :
                        estado = "e</nom"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</nom":
                    if letra == "b" or letra == "B" :
                        estado = "e</nomb"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</nomb":
                    if letra == "r" or letra == "R" :
                        estado = "e</nombr"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</nombr":
                    if letra == "E" or letra == "e" :
                        estado = "e</nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</nombre":
                    if letra == ">" :
                        estado = "estacion_apertura"
                    elif letra == " ":
                        continue
                    
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
            
                #ESTADO
                elif estado == "e<e":
                    if letra == "s" or letra == "S":
                        estado = "e<es"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<es":
                    if letra == "t" or letra == "T":
                        estado = "e<est"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<est":
                    if letra == "a" or letra == "A":
                        estado = "e<esta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<esta":
                    if letra == "d" or letra == "D":
                        estado = "e<estad"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<estad":
                    if letra == "o" or letra == "O":
                        estado = "e<estado"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<estado":
                    if letra == ">":
                        estado = "e<estado>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<estado>":
                    if letra == "\n":
                        estado = "e_estado_primera_letra"
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "estacion_estado"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e_estado_primera_letra":
                    if letra == " ":
                        continue
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "estacion_estado"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "estacion_estado":
                    if re.search(pattern_nombre, letra) :
                        continue
                    elif letra == " ":
                        continue
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "estacion_EstadoCierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "estacion_EstadoCierre":
                    if letra == "/" :
                        estado = "estacion_EstadoCierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "estacion_EstadoCierre/":
                    if letra == "e" or letra =="E" :
                        estado = "e</e"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</e":
                    if letra == "s" or letra == "S" :
                        estado = "e</es"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</es":
                    if letra == "t" or letra == "T" :
                        estado = "e</est"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</est":
                    if letra == "a" or letra == "A" :
                        estado = "e</esta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</esta":
                    if letra == "d" or letra == "D" :
                        estado = "e</estad"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</estad":
                    if letra == "o" or letra == "O" :
                        estado = "e</estado"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</estado":
                    if letra == ">" :
                        estado = "estacion_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                #Color
                elif estado == "e<c":
                    if letra == "o" or letra == "O":
                        estado = "e<co"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<co":
                    if letra == "l" or letra == "L":
                        estado = "e<col"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<col":
                    if letra == "o" or letra == "O":
                        estado = "e<colo"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<colo":
                    if letra == "r" or letra == "R":
                        estado = "e<color"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")

                elif estado == "e<color":
                    if letra == ">":
                        estado = "e<color>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e<color>":
                    if letra == "\n":
                        estado = "e_color_primera_letra"
                    elif letra == "#":
                        estado = "estacion_color"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e_color_primera_letra":
                    if letra == " ":
                        continue
                    elif letra == "#":
                        estado = "estacion_color"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "estacion_color":
                    if re.search(r"[A-Za-z0-9]", letra) :
                        continue
                    elif letra == " ":
                        continue
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "estacion_ColorCierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "estacion_ColorCierre":
                    if letra == "/" :
                        estado = "estacion_ColorCierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "estacion_ColorCierre/":
                    if letra == "c" or letra =="C" :
                        estado = "e</c"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</c":
                    if letra == "o" or letra == "O" :
                        estado = "e</co"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</co":
                    if letra == "l" or letra == "L" :
                        estado = "e</col"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</col":
                    if letra == "o" or letra == "O" :
                        estado = "e</colo"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</colo":
                    if letra == "r" or letra == "R" :
                        estado = "e</color"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</color":
                    if letra == ">" :
                        estado = "estacion_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
            

                #EstacionCierre
                elif estado == "e</":
                    if letra == "e" or letra =="E" :
                        estado = "e</e"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</e":
                    if letra == "s" or letra == "S" :
                        estado = "e</es"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</es":
                    if letra == "t" or letra == "T" :
                        estado = "e</est"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</est":
                    if letra == "a" or letra == "A" :
                        estado = "e</esta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</esta":
                    if letra == "c" or letra == "C" :
                        estado = "e</estac"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</estac":
                    if letra == "i" or letra == "I" :
                        estado = "e</estaci"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</estaci":
                    if letra == "o" or letra == "O" :
                        estado = "e</estacio"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "e</estacio":
                    if letra == "n" or letra == "N" :
                        estado = "e</estacion"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "e</estacion":
                    if letra == ">" :
                        estado = "nada"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
            n_linea += 1
                
                
            
analizar_archivo("das.txt")