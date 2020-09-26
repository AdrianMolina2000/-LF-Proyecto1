import re, os

file_name = open("Reporte/index.html", "w")
  
def html(n_linea, n_letra, letra):
    file_name.write("           <tr>\n")
    file_name.write(f"                <th>{n_linea}</th>\n")
    file_name.write(f"                <th>{n_letra}</th>\n")
    file_name.write(f"                <th>{letra}</th>\n")
    file_name.write("           </tr>\n")

def analizar_archivo_error(path):
    #Reporte
    file_name.write("<!DOCTYPE html>\n<html>\n<head>\n")
    file_name.write("   <meta charset='UTF-8'>\n")
    file_name.write("   <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css'>\n")
    file_name.write("</head>\n")
    file_name.write("<body class='container'>\n")
    file_name.write("   <table class='striped'>\n")
    file_name.write("       <thead>\n")
    file_name.write("           <tr>\n")
    file_name.write("               <th>Linea</th>\n")
    file_name.write("               <th>Columna</th>\n")
    file_name.write("               <th>Caracter</th>\n")
    file_name.write("           </tr>\n")
    file_name.write("       </thead>\n")
    file_name.write("       <tbody>\n")
    

    #Errores
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
                        html(n_linea, n_letra, letra)
                        
                elif estado == "<":
                    if letra == " ":
                        continue
                    #RUTA
                    elif letra == "R" or letra == "r":
                        estado = "<r"
                    
                    #ESTACION
                    elif letra == "e" or letra == "E":
                        estado = "<e"
                    
                    #NOMBRE MAPA
                    elif letra == "n" or letra == "N":
                        estado = "<n"
                    
                    else:
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                #RUTA
                elif estado == "<r":
                    if letra == "u" or letra == "U":
                        estado = "<ru"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<ru":
                    if letra == "T" or letra == "t":
                        estado = "<rut"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<rut":
                    if letra == "a" or letra == "A":
                        estado = "<ruta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<ruta":
                    if letra == ">":
                        estado = "<ruta>"
                    elif letra == " ":
                        estado = "<ruta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<ruta>":
                    if letra == "\n":
                        estado = "ruta_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "ruta_apertura":
                    if letra == "<":
                        estado = "r<"
                    elif letra == " ":
                        continue
                    elif letra == "\n":
                        continue
                    else:
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
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
                        html(n_linea, n_letra, letra)
                            
                
                elif estado == "r<n":
                    if letra == "o" or letra == "O":
                        estado = "r<no"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<no":
                    if letra == "m" or letra == "M":
                        estado = "r<nom"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<nom":
                    if letra == "b" or letra == "B":
                        estado = "r<nomb"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<nomb":
                    if letra == "r" or letra == "R":
                        estado = "r<nombr"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<nombr":
                    if letra == "e" or letra == "E":
                        estado = "r<nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<nombre":
                    if letra == ">":
                        estado = "r<nombre>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<nombre>":
                    if letra == "\n":
                        estado = "r_nombre_primera_letra"
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "ruta_nombre"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r_nombre_primera_letra":
                    if letra == " ":
                        continue
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "ruta_nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "ruta_nombre":
                    if re.search(pattern_nombre, letra) :
                        continue
                    elif letra == " ":
                        estado = "fin_ruta_nombre"
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "ruta_nombreCierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "fin_ruta_nombre":
                    if letra == "<":
                        estado = "ruta_nombreCierre"
                    elif letra == "\n":
                        continue
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)

                elif estado == "ruta_nombreCierre":
                    if letra == "/" :
                        estado = "ruta_nombreCierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "ruta_nombreCierre/":
                    if letra == "n" or letra =="N" :
                        estado = "r</n"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</n":
                    if letra == "o" or letra == "O" :
                        estado = "r</no"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</no":
                    if letra == "m" or letra == "M" :
                        estado = "r</nom"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</nom":
                    if letra == "b" or letra == "B" :
                        estado = "r</nomb"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</nomb":
                    if letra == "r" or letra == "R" :
                        estado = "r</nombr"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</nombr":
                    if letra == "E" or letra == "e" :
                        estado = "r</nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</nombre":
                    if letra == ">" :
                        estado = "ruta_apertura"
                    elif letra == " ":
                        continue
                    
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                


                #PESO
                elif estado == "r<p":
                    if letra == "e" or letra == "E":
                        estado = "r<pe"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<pe":
                    if letra == "s" or letra == "S":
                        estado = "r<pes"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<pes":
                    if letra == "o" or letra == "O":
                        estado = "r<peso"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<peso":
                    if letra == ">":
                        estado = "r<peso>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<peso>":
                    if letra == "\n":
                        estado = "peso_antes"
                    elif re.search(r"[0-9]", letra):
                        estado = "peso_antes"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "peso_antes":
                    if letra == ".":
                        estado = "punto"
                    elif letra == "<":
                        estado = "Peso_Cierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "punto":
                    if re.search(r"[0-9]", letra) :
                        estado = "peso_post"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "peso_post":
                    if re.search(r"[0-9]", letra) :
                        estado = "peso_post"
                    elif letra == " " :
                        estado = "fin_peso"
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "Peso_Cierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)

                elif estado == "fin_peso":
                    if letra == "<":
                        estado = "Peso_Cierre"
                    elif letra == "\n":
                        continue
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")  
                        html(n_linea, n_letra, letra)  
                elif estado == "Peso_Cierre":
                    if letra == "/" :
                        estado = "Peso_Cierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "Peso_Cierre/":
                    if letra == "p" or letra =="P" :
                        estado = "r</p"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</p":
                    if letra == "e" or letra == "E" :
                        estado = "r</pe"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</pe":
                    if letra == "s" or letra == "S" :
                        estado = "r</pes"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</pes":
                    if letra == "o" or letra == "O" :
                        estado = "r</peso"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</peso":
                    if letra == ">" :
                        estado = "ruta_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
            
                #INICIO
                elif estado == "r<i":
                    if letra == "n" or letra == "N":
                        estado = "r<in"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<in":
                    if letra == "i" or letra == "I":
                        estado = "r<ini"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<ini":
                    if letra == "c" or letra == "C":
                        estado = "r<inic"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<inic":
                    if letra == "i" or letra == "I":
                        estado = "r<inici"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<inici":
                    if letra == "o" or letra == "O":
                        estado = "r<inicio"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<inicio":
                    if letra == ">":
                        estado = "r<inicio>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<inicio>":
                    if letra == "\n":
                        estado = "r_inicio_primera_letra"
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "ruta_inicio"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r_inicio_primera_letra":
                    if letra == " ":
                        continue
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "ruta_inicio"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "ruta_inicio":
                    if re.search(pattern_nombre, letra) :
                        continue
                    elif letra == " ":
                        estado = "fin_inicio"
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "ruta_InicioCierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "fin_inicio":
                    if letra == "<":
                        estado = "ruta_InicioCierre"
                    elif letra == "\n":
                        continue
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "ruta_InicioCierre":
                    if letra == "/" :
                        estado = "ruta_InicioCierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "ruta_InicioCierre/":
                    if letra == "i" or letra =="I" :
                        estado = "r</i"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</i":
                    if letra == "n" or letra == "N" :
                        estado = "r</in"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</in":
                    if letra == "i" or letra == "I" :
                        estado = "r</ini"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</ini":
                    if letra == "c" or letra == "C" :
                        estado = "r</inic"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</inic":
                    if letra == "i" or letra == "I" :
                        estado = "r</inici"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</inici":
                    if letra == "o" or letra == "O" :
                        estado = "r</inicio"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</inicio":
                    if letra == ">" :
                        estado = "ruta_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                
                
                #FIN
                elif estado == "r<f":
                    if letra == "i" or letra == "I":
                        estado = "r<fi"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<fi":
                    if letra == "n" or letra == "N":
                        estado = "r<fin"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<fin":
                    if letra == ">":
                        estado = "r<fin>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r<fin>":
                    if letra == "\n":
                        estado = "r_fin_primera_letra"
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "ruta_fin"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r_fin_primera_letra":
                    if letra == " ":
                        continue
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "ruta_fin"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "ruta_fin":
                    if re.search(pattern_nombre, letra) :
                        continue
                    elif letra == " ":
                        estado = "fin_ruta_fin"
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "ruta_FinCierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "fin_ruta_fin":
                    if letra == "<":
                        estado = "ruta_FinCierre"
                    elif letra == "\n":
                        continue
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "ruta_FinCierre":
                    if letra == "/" :
                        estado = "ruta_FinCierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "ruta_FinCierre/":
                    if letra == "f" or letra =="F" :
                        estado = "r</f"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</f":
                    if letra == "i" or letra == "I" :
                        estado = "r</fi"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</fi":
                    if letra == "n" or letra == "N" :
                        estado = "r</fin"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)                
                elif estado == "r</fin":
                    if letra == ">" :
                        estado = "ruta_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)



                #RutaCierre
                elif estado == "r</":
                    if letra == "r" or letra =="R" :
                        estado = "r</r"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</r":
                    if letra == "u" or letra == "U" :
                        estado = "r</ru"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</ru":
                    if letra == "t" or letra == "T" :
                        estado = "r</rut"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</rut":
                    if letra == "a" or letra == "A" :
                        estado = "r</ruta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "r</ruta":
                    if letra == ">" :
                        estado = "nada"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)


                #Estacion
                elif estado == "<e":
                    if letra == "s" or letra == "S":
                        estado = "<es"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "<es":
                    if letra == "T" or letra == "t":
                        estado = "<est"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<est":
                    if letra == "a" or letra == "A":
                        estado = "<esta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<esta":
                    if letra == "c" or letra == "C":
                        estado = "<estac"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<estac":
                    if letra == "i" or letra == "I":
                        estado = "<estaci"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<estaci":
                    if letra == "o" or letra == "O":
                        estado = "<estacio"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<estacio":
                    if letra == "n" or letra == "N":
                        estado = "<estacion"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)

                elif estado == "<estacion":
                    if letra == ">":
                        estado = "<estacion>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<estacion>":
                    if letra == "\n":
                        estado = "estacion_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "estacion_apertura":
                    if letra == "<":
                        estado = "e<"
                    elif letra == " ":
                        continue
                    elif letra == "\n":
                        continue
                    else:
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "e<":
                    #nombre
                    if letra == "n" or letra == "N":
                        estado = "e<n"

                    #estado
                    elif letra == "e" or letra == "E":
                        estado = "e<e"

                    #color
                    elif letra == "c" or letra == "C":
                        estado = "e<c"
                    
                    #estacionCierre
                    elif letra == "/":
                        estado = "es</"
                    
                    elif letra == "\n":
                        continue

                    else:
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)

                #Estacion
                elif estado == "e<n":
                    if letra == "o" or letra == "O":
                        estado = "e<no"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<no":
                    if letra == "m" or letra == "M":
                        estado = "e<nom"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<nom":
                    if letra == "b" or letra == "B":
                        estado = "e<nomb"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<nomb":
                    if letra == "r" or letra == "R":
                        estado = "e<nombr"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<nombr":
                    if letra == "e" or letra == "E":
                        estado = "e<nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<nombre":
                    if letra == ">":
                        estado = "e<nombre>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<nombre>":
                    if letra == "\n":
                        estado = "e_nombre_primera_letra"
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "estacion_nombre"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e_nombre_primera_letra":
                    if letra == " ":
                        continue
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "estacion_nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "estacion_nombre":
                    if re.search(pattern_nombre, letra) :
                        continue
                    elif letra == " ":
                        estado = "fin_estacion_nombre"
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "estacion_nombreCierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "fin_estacion_nombre":
                    if letra == "<":
                        estado = "estacion_nombreCierre"
                    elif letra == "\n":
                        continue
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "estacion_nombreCierre":
                    if letra == "/" :
                        estado = "estacion_nombreCierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "estacion_nombreCierre/":
                    if letra == "n" or letra =="N" :
                        estado = "e</n"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</n":
                    if letra == "o" or letra == "O" :
                        estado = "e</no"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</no":
                    if letra == "m" or letra == "M" :
                        estado = "e</nom"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</nom":
                    if letra == "b" or letra == "B" :
                        estado = "e</nomb"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</nomb":
                    if letra == "r" or letra == "R" :
                        estado = "e</nombr"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</nombr":
                    if letra == "E" or letra == "e" :
                        estado = "e</nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</nombre":
                    if letra == ">" :
                        estado = "estacion_apertura"
                    elif letra == " ":
                        continue
                    
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
            
                #ESTADO
                elif estado == "e<e":
                    if letra == "s" or letra == "S":
                        estado = "e<es"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<es":
                    if letra == "t" or letra == "T":
                        estado = "e<est"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<est":
                    if letra == "a" or letra == "A":
                        estado = "e<esta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<esta":
                    if letra == "d" or letra == "D":
                        estado = "e<estad"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<estad":
                    if letra == "o" or letra == "O":
                        estado = "e<estado"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<estado":
                    if letra == ">":
                        estado = "e<estado>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<estado>":
                    if letra == "\n":
                        estado = "e_estado_primera_letra"
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "estacion_estado"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e_estado_primera_letra":
                    if letra == " ":
                        continue
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "estacion_estado"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "estacion_estado":
                    if re.search(pattern_nombre, letra) :
                        continue
                    elif letra == " ":
                        estado = "estado_fin"
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "estacion_EstadoCierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "estado_fin":
                    if letra == "<":
                        estado = "estacion_EstadoCierre"
                    elif letra == "\n":
                        continue
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "estacion_EstadoCierre":
                    if letra == "/" :
                        estado = "estacion_EstadoCierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "estacion_EstadoCierre/":
                    if letra == "e" or letra =="E" :
                        estado = "e</e"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</e":
                    if letra == "s" or letra == "S" :
                        estado = "e</es"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</es":
                    if letra == "t" or letra == "T" :
                        estado = "e</est"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</est":
                    if letra == "a" or letra == "A" :
                        estado = "e</esta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</esta":
                    if letra == "d" or letra == "D" :
                        estado = "e</estad"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</estad":
                    if letra == "o" or letra == "O" :
                        estado = "e</estado"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</estado":
                    if letra == ">" :
                        estado = "estacion_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                #Color
                elif estado == "e<c":
                    if letra == "o" or letra == "O":
                        estado = "e<co"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<co":
                    if letra == "l" or letra == "L":
                        estado = "e<col"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<col":
                    if letra == "o" or letra == "O":
                        estado = "e<colo"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<colo":
                    if letra == "r" or letra == "R":
                        estado = "e<color"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)

                elif estado == "e<color":
                    if letra == ">":
                        estado = "e<color>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e<color>":
                    if letra == "\n":
                        estado = "e_color_primera_letra"
                    elif letra == "#":
                        estado = "estacion_color"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e_color_primera_letra":
                    if letra == " ":
                        continue
                    elif letra == "#":
                        estado = "estacion_color"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "estacion_color":
                    if re.search(r"[A-Za-z0-9]", letra) :
                        continue
                    elif letra == " ":
                        estado = "fin_color"
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "estacion_ColorCierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "fin_color":
                    if letra == "<":
                        estado = "estacion_ColorCierre"
                    elif letra == "\n":
                        continue
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "estacion_ColorCierre":
                    if letra == "/" :
                        estado = "estacion_ColorCierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "estacion_ColorCierre/":
                    if letra == "c" or letra =="C" :
                        estado = "e</c"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</c":
                    if letra == "o" or letra == "O" :
                        estado = "e</co"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</co":
                    if letra == "l" or letra == "L" :
                        estado = "e</col"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</col":
                    if letra == "o" or letra == "O" :
                        estado = "e</colo"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</colo":
                    if letra == "r" or letra == "R" :
                        estado = "e</color"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "e</color":
                    if letra == ">" :
                        estado = "estacion_apertura"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
            
                #EstacionCierre
                elif estado == "es</":
                    if letra == "e" or letra =="E" :
                        estado = "es</e"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "es</e":
                    if letra == "s" or letra == "S" :
                        estado = "es</es"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "es</es":
                    if letra == "t" or letra == "T" :
                        estado = "es</est"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "es</est":
                    if letra == "a" or letra == "A" :
                        estado = "es</esta"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "es</esta":
                    if letra == "c" or letra == "C" :
                        estado = "es</estac"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "es</estac":
                    if letra == "i" or letra == "I" :
                        estado = "es</estaci"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "es</estaci":
                    if letra == "o" or letra == "O" :
                        estado = "es</estacio"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "es</estacio":
                    if letra == "n" or letra == "N" :
                        estado = "es</estacion"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "es</estacion":
                    if letra == ">" :
                        estado = "nada"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                

                #Nombre Mapa
                elif estado == "<n":
                    if letra == "o" or letra == "O":
                        estado = "<no"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "<no":
                    if letra == "m" or letra == "M":
                        estado = "<nom"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<nom":
                    if letra == "b" or letra == "B":
                        estado = "<nomb"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<nomb":
                    if letra == "r" or letra == "R":
                        estado = "<nombr"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<nombr":
                    if letra == "e" or letra == "e":
                        estado = "<nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)

                elif estado == "<nombre":
                    if letra == ">":
                        estado = "<nombre>"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "<nombre>":
                    if letra == "\n":
                        estado = "nombre_primera_letra"
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "nombre_primera_letra"    
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "nombre_primera_letra":
                    if letra == " ":
                        continue
                    elif re.search(pattern_primera_Letra, letra):
                        estado = "nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                
                elif estado == "nombre":
                    if re.search(pattern_nombre, letra) :
                        continue
                    elif letra == " ":
                        continue
                    elif letra == "\n":
                        continue
                    elif letra == "<":
                        estado = "nombreCierre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "nombreCierre":
                    if letra == "/" :
                        estado = "nombreCierre/"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "nombreCierre/":
                    if letra == "n" or letra =="N" :
                        estado = "</n"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "</n":
                    if letra == "o" or letra == "O" :
                        estado = "</no"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "</no":
                    if letra == "m" or letra == "M" :
                        estado = "</nom"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "</nom":
                    if letra == "b" or letra == "B" :
                        estado = "</nomb"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "</nomb":
                    if letra == "r" or letra == "R" :
                        estado = "</nombr"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "</nombr":
                    if letra == "E" or letra == "e" :
                        estado = "</nombre"
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
                elif estado == "</nombre":
                    if letra == ">" :
                        estado = "nada"
                    elif letra == " ":
                        continue
                    else: 
                        print(f"||linea: {n_linea}||columna {n_letra}||valor: {letra}||")
                        html(n_linea, n_letra, letra)
            n_linea += 1
    file_name.write("       </tbody>\n")
    file_name.write("   </table>\n")
    file_name.write("</body>\n</html>\n")
    os.startfile("Reporte\index.html")
    file_name.close()
                

