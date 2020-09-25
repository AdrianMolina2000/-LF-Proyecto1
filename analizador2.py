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
                elif estado == "r<n":
                    if letra == "o" or letra == "O":
                        estado = "r<no"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<no":
                    if letra == "m" or letra == "M":
                        estado = "r<nom"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<nom":
                    if letra == "b" or letra == "B":
                        estado = "r<nomb"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<nomb":
                    if letra == "r" or letra == "R":
                        estado = "r<nombr"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<nombr":
                    if letra == "e" or letra == "E":
                        estado = "r<nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<nombre":
                    if letra == ">":
                        estado = "r<nombre>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<nombre>":
                    if letra == "\n":
                        estado = "r_nombre_primera_letra"
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "ruta_nombre"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r_nombre_primera_letra":
                    if letra == " ":
                        continue
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "ruta_nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "ruta_nombre":
                    if re.search(pattern_nombre, letra) :
                        continue
                    elif letra == " ":
                        continue
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "ruta_nombreCierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "ruta_nombreCierre":
                    if letra == "/" :
                        estado = "ruta_nombreCierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "ruta_nombreCierre/":
                    if letra == "n" or letra =="N" :
                        estado = "r</n"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</n":
                    if letra == "o" or letra == "O" :
                        estado = "r</no"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</no":
                    if letra == "m" or letra == "M" :
                        estado = "r</nom"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</nom":
                    if letra == "b" or letra == "B" :
                        estado = "r</nomb"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</nomb":
                    if letra == "r" or letra == "R" :
                        estado = "r</nombr"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</nombr":
                    if letra == "E" or letra == "e" :
                        estado = "r</nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</nombre":
                    if letra == ">" :
                        estado = "ruta_apertura"
                    elif letra == " ":
                        continue
                    
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                


                #PESO
                elif estado == "r<p":
                    if letra == "e" or letra == "E":
                        estado = "r<pe"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<pe":
                    if letra == "s" or letra == "S":
                        estado = "r<pes"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<pes":
                    if letra == "o" or letra == "O":
                        estado = "r<peso"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<peso":
                    if letra == ">":
                        estado = "r<peso>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<peso>":
                    if letra == "\n":
                        estado = "peso_antes"
                    elif re.search(r"[0-9]", letra):
                        estado = "peso_antes"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "peso_antes":
                    if letra == ".":
                        estado = "punto"
                    elif letra == "<":
                        estado = "Peso_Cierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "punto":
                    if re.search(r"[0-9]", letra) :
                        estado = "peso_post"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "peso_post":
                    if re.search(r"[0-9]", letra) :
                        estado = "peso_post"
                    elif letra == " " :
                        continue
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "Peso_Cierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "Peso_Cierre":
                    if letra == "/" :
                        estado = "Peso_Cierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "Peso_Cierre/":
                    if letra == "p" or letra =="P" :
                        estado = "r</p"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</p":
                    if letra == "e" or letra == "E" :
                        estado = "r</pe"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</pe":
                    if letra == "s" or letra == "S" :
                        estado = "r</pes"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</pes":
                    if letra == "o" or letra == "O" :
                        estado = "r</peso"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</peso":
                    if letra == ">" :
                        estado = "ruta_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
            
                #INICIO
                elif estado == "r<i":
                    if letra == "n" or letra == "N":
                        estado = "r<in"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<in":
                    if letra == "i" or letra == "I":
                        estado = "r<ini"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<ini":
                    if letra == "c" or letra == "C":
                        estado = "r<inic"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<inic":
                    if letra == "i" or letra == "I":
                        estado = "r<inici"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<inici":
                    if letra == "o" or letra == "O":
                        estado = "r<inicio"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<inicio":
                    if letra == ">":
                        estado = "r<inicio>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<inicio>":
                    if letra == "\n":
                        estado = "r_inicio_primera_letra"
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "ruta_inicio"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r_inicio_primera_letra":
                    if letra == " ":
                        continue
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "ruta_inicio"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "ruta_inicio":
                    if re.search(pattern_nombre, letra) :
                        continue
                    elif letra == " ":
                        continue
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "ruta_InicioCierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "ruta_InicioCierre":
                    if letra == "/" :
                        estado = "ruta_InicioCierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "ruta_InicioCierre/":
                    if letra == "i" or letra =="I" :
                        estado = "r</i"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</i":
                    if letra == "n" or letra == "N" :
                        estado = "r</in"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</in":
                    if letra == "i" or letra == "I" :
                        estado = "r</ini"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</ini":
                    if letra == "c" or letra == "C" :
                        estado = "r</inic"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</inic":
                    if letra == "i" or letra == "I" :
                        estado = "r</inici"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</inici":
                    if letra == "o" or letra == "O" :
                        estado = "r</inicio"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</inicio":
                    if letra == ">" :
                        estado = "ruta_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                
                
                #FIN
                elif estado == "r<f":
                    if letra == "i" or letra == "I":
                        estado = "r<fi"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<fi":
                    if letra == "n" or letra == "N":
                        estado = "r<fin"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<fin":
                    if letra == ">":
                        estado = "r<fin>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r<fin>":
                    if letra == "\n":
                        estado = "r_fin_primera_letra"
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "ruta_fin"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r_fin_primera_letra":
                    if letra == " ":
                        continue
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "ruta_fin"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                
                elif estado == "ruta_fin":
                    if re.search(pattern_nombre, letra) :
                        continue
                    elif letra == " ":
                        continue
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "ruta_FinCierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "ruta_FinCierre":
                    if letra == "/" :
                        estado = "ruta_FinCierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "ruta_FinCierre/":
                    if letra == "f" or letra =="F" :
                        estado = "r</f"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</f":
                    if letra == "i" or letra == "I" :
                        estado = "r</fi"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</fi":
                    if letra == "n" or letra == "N" :
                        estado = "r</fin"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")                
                elif estado == "r</fin":
                    if letra == ">" :
                        estado = "ruta_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")



                #RutaCierre
                elif estado == "r</":
                    if letra == "r" or letra =="R" :
                        estado = "r</r"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</r":
                    if letra == "u" or letra == "U" :
                        estado = "r</ru"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</ru":
                    if letra == "t" or letra == "T" :
                        estado = "r</rut"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</rut":
                    if letra == "a" or letra == "A" :
                        estado = "r</ruta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                elif estado == "r</ruta":
                    if letra == ">" :
                        estado = "nada"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
            n_linea += 1
                
                
            
analizar_archivo("das.txt")