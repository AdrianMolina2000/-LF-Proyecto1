import re

def analizar_archivo(path):
    file_name = open("corregido.txt", "w")
    #Ruta
    pattern_ruta_apertura = r"<[^/]*[R|r][U|u][T|t][A|a](.)*>"

    pattern_ruta_nombre_apertura = r"<[^/]*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
    pattern_ruta_nombre_contenido_entre = r">[A-Za-z]+[_|A-Za-z0-9|@|#]*<"
    pattern_ruta_nombre_contenido_post = r"[A-Za-z]+[_|A-Za-z0-9|@|#]*"
    pattern_ruta_nombre_cerradura = r"</(.)*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"

    pattern_ruta_inicio_apertura = r"<[^/]*[I|i][N|n][I|i][C|c][I|i][O|o](.)*>"
    pattern_ruta_inicio_contenido_entre = r">[A-Za-z]+[_|A-Za-z0-9|@|#]*<"
    pattern_ruta_inicio_contenido_post = r"[A-Za-z]+[_|A-Za-z0-9|@|#]*"
    pattern_ruta_inicio_cerradura = r"</(.)*[I|i][N|n][I|i][C|c][I|i][O|o](.)*>"

    pattern_ruta_fin_apertura = r"<[^/]*[F|f][I|i][N|n](.)*>"
    pattern_ruta_fin_contenido_entre = r">[A-Za-z]+[_|A-Za-z0-9|@|#]*<"
    pattern_ruta_fin_contenido_post = r"[A-Za-z]+[_|A-Za-z0-9|@|#]*"
    pattern_ruta_fin_cerradura = r"</(.)*[F|f][I|i][N|n](.)*>"

    pattern_ruta_peso_apertura = r"<[^/]*[P|p][E|e][S|s][O|o](.)*>"
    pattern_ruta_peso_contenido_entre = r">[0-9]+[.]?[0-9]*<"
    pattern_ruta_peso_contenido_post = r"[0-9]+[.]?[0-9]*"
    pattern_ruta_peso_cerradura = r"</(.)*[P|p][E|e][S|s][O|o](.)*>"
    pattern_ruta_cerradura = r"</(.)*[R|r][U|u][T|t][A|a](.)*>"

    pattern_estacion_apertura = r"<[^/]*[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n](.)*>"
    
    pattern_estacion_nombre_apertura = r"<[^/]*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
    pattern_estacion_nombre_contenido_entre = r">[A-Za-z]+[_|A-Za-z0-9|@|#]*<"
    pattern_estacion_nombre_contenido_post = r"[A-Za-z]+[_|A-Za-z0-9|@|#]*"
    pattern_estacion_nombre_cerradura = r"</(.)*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"

    pattern_estacion_estado_apertura = r"<[^/]*[E|e][S|s][T|t][A|a][D|d][O|o](.)*>"
    pattern_estacion_estado1_contenido_entre = r">[D|d][I|i][S|s][P|p][O|o][N|n][I|i][B|b][L|l][E|e]<"
    pattern_estacion_estado1_contenido_post = r"[D|d][I|i][S|s][P|p][O|o][N|n][I|i][B|b][L|l][E|e]"
    pattern_estacion_estado2_contenido_entre = r">[C|c][E|e][R|r][R|r][A|a][D|d][A|a|O|o]<"
    pattern_estacion_estado2_contenido_post = r"[C|c][E|e][R|r][R|r][A|a][D|d][A|a|O|o]"
    pattern_estacion_estado_cerradura = r"</(.)*[E|e][S|s][T|t][A|a][D|d][O|o](.)*>"

    pattern_estacion_color_apertura = r"<[^/]*[C|c][O|o][L|l][O|o][R|r](.)*>"
    pattern_estacion_color_contenido_entre = r">#[A-Z0-9]{6,6}<"
    pattern_estacion_color_contenido_post = r"#[A-Z0-9]{6,6}"
    pattern_estacion_color_cerradura = r"</(.)*[C|c][O|o][L|l][O|o][R|r](.)*>"

    pattern_estacion_cerradura = r"</(.)*[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n](.)*>"
    
    pattern_nombre_apertura = r"<[^/]*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
    pattern_nombre_contenido_entre = r">[A-Za-z]+[_|A-Za-z0-9|@|#|\s]*<"
    pattern_nombre_contenido_post = r"[A-Za-z]+[_|A-Za-z0-9|@|#|\s]*"
    pattern_nombre_cerradura = r"</(.)*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"

    estado = "nada"

    with open(path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        for i in lineas:
            
            #Nivel1
            if estado == "nada": 
                if re.search(pattern_ruta_apertura, i):
                    estado = "ruta_apertura"
                    file_name.write("<ruta>\n")

                elif re.search(pattern_estacion_apertura, i):
                    estado = "estacion_apertura"
                    file_name.write("<estacion>\n")
                
                elif re.search(pattern_nombre_apertura, i):
                    if re.search(pattern_nombre_cerradura, i):
                        estado = "nombre_apertura"
                        file_name.write("<nombre>\n")
                        if re.search(pattern_nombre_contenido_entre, i):
                            nombre1 = re.findall(pattern_nombre_contenido_entre,i)[0]
                            nombre1 = nombre1.replace("<","")
                            nombre1 = nombre1.replace(">","")
                        file_name.write(r"       "+nombre1+"\n")
                        file_name.write("</nombre>\n")

                    else:
                        estado = "nombre_apertura"
                        file_name.write("<nombre>\n")
                else:
                    estado = "nada"



            elif estado == "ruta_apertura":

                if re.search(pattern_ruta_nombre_apertura, i):
                    if re.search(pattern_ruta_nombre_cerradura, i):
                        estado = "ruta_apertura"
                        file_name.write("   <nombre>\n")
                        if re.search(pattern_ruta_nombre_contenido_entre, i):
                            nombre1 = re.findall(pattern_ruta_nombre_contenido_entre, i)[0]
                            nombre1 = nombre1.replace(">", "")
                            nombre1 = nombre1.replace("<", "")
                            file_name.write("       "+ nombre1 +"\n")
                        file_name.write("   </nombre>\n")
                    else:
                        estado = "ruta_nombre_apertura"
                        file_name.write("   <nombre>\n")
                        
                
                elif re.search(pattern_ruta_inicio_apertura, i):
                    if re.search(pattern_ruta_inicio_cerradura, i):
                        estado = "ruta_apertura"
                        file_name.write("   <inicio>\n")
                        if re.search(pattern_ruta_inicio_contenido_entre, i):
                            inicio1 = re.findall(pattern_ruta_inicio_contenido_entre, i)[0]
                            inicio1 = inicio1.replace(">", "")
                            inicio1 = inicio1.replace("<", "")
                            file_name.write("       "+ inicio1 +"\n")
                        file_name.write("   </inicio>\n")
                    else:
                        estado = "ruta_inicio_apertura"
                        file_name.write("   <inicio>\n")
                
                elif re.search(pattern_ruta_fin_apertura, i):
                    if re.search(pattern_ruta_fin_cerradura, i):
                        estado = "ruta_apertura"
                        file_name.write("   <fin>\n")
                        if re.search(pattern_ruta_fin_contenido_entre, i):
                            fin1 = re.findall(pattern_ruta_fin_contenido_entre, i)[0]
                            fin1 = fin1.replace(">", "")
                            fin1 = fin1.replace("<", "")
                            file_name.write("       "+ fin1 +"\n")
                        file_name.write("   </fin>\n")
                    else:
                        estado = "ruta_fin_apertura"
                        file_name.write("   <fin>\n")
                        
                
                elif re.search(pattern_ruta_peso_apertura, i):
                    if re.search(pattern_ruta_peso_cerradura,i):
                        estado = "ruta_apertura"
                        file_name.write("   <peso>\n")
                        if re.search(pattern_ruta_peso_contenido_entre, i):
                            peso1 = re.findall(pattern_ruta_peso_contenido_entre,i)[0]
                            peso1 = peso1.replace("<","")
                            peso1 = peso1.replace(">","")
                            file_name.write(r"       "+peso1+"\n")
                        
                        file_name.write("   </peso>\n")
                    else:
                        estado = "ruta_peso_apertura"
                        file_name.write("   <peso>\n")

                elif re.search(pattern_ruta_cerradura, i):
                    estado = "nada"
                    file_name.write("</ruta>\n")
            


            elif estado == "estacion_apertura":
                if re.search(pattern_estacion_nombre_apertura, i):
                    if re.search(pattern_estacion_nombre_cerradura, i):
                        estado = "estacion_apertura"
                        file_name.write("   <nombre>\n")

                        if re.search(pattern_estacion_nombre_contenido_entre, i):
                            nombre1 = re.findall(pattern_estacion_nombre_contenido_entre,i)[0]
                            nombre1 = nombre1.replace("<","")
                            nombre1 = nombre1.replace(">","")
                        file_name.write(r"       "+nombre1+"\n")
                        file_name.write("   </nombre>\n")

                    else:
                        estado = "estacion_nombre_apertura"
                        file_name.write("   <nombre>\n")
                
                elif re.search(pattern_estacion_estado_apertura, i):
                    if re.search(pattern_estacion_estado_cerradura, i):
                        estado = "estacion_apertura"
                        file_name.write("   <estado>\n")
                        if re.search(pattern_estacion_estado1_contenido_entre, i):
                            estado1 = re.findall(pattern_estacion_estado1_contenido_entre,i)[0]
                            estado1 = estado1.replace("<","")
                            estado1 = estado1.replace(">","")
                        if re.search(pattern_estacion_estado2_contenido_entre, i):
                            estado1 = re.findall(pattern_estacion_estado2_contenido_entre,i)[0]
                            estado1 = estado1.replace("<","")
                            estado1 = estado1.replace(">","")
                        file_name.write(r"       "+estado1+"\n")
                        file_name.write("   </estado>\n")

                    else:
                        estado = "estacion_estado_apertura"
                        file_name.write("   <estado>\n")
                
                elif re.search(pattern_estacion_color_apertura, i):
                    if re.search(pattern_estacion_color_cerradura, i):
                        estado = "estacion_apertura"
                        file_name.write("   <color>\n")
                        if re.search(pattern_estacion_color_contenido_entre, i):
                            color1 = re.findall(pattern_estacion_color_contenido_entre,i)[0]
                            color1 = color1.replace("<","")
                            color1 = color1.replace(">","")
                        file_name.write(r"       "+color1+"\n")
                        file_name.write("   </color>\n")

                    else:
                        estado = "estacion_color_apertura"
                        file_name.write("   <color>\n")

                elif re.search(pattern_estacion_cerradura, i):
                    estado = "nada"
                    file_name.write("</estacion>\n")


            elif estado == "nombre_apertura":
                if re.search(pattern_nombre_cerradura, i):
                    estado = "nada"
                    file_name.write("</nombre>\n")
                
                elif re.search(pattern_nombre_contenido_post, i):
                    nombre2 = i.replace("\n", "")
                    nombre2 = nombre2.replace(" ", "")
                    nombre1 = re.findall(pattern_nombre_contenido_post, estado2)[0]
                    file_name.write("       "+ nombre1 +"\n")
                    estado == "nombre_apertura"




            #Nivel 2
            elif estado == "ruta_nombre_apertura":
                
                if re.search(pattern_ruta_nombre_cerradura, i):
                    estado = "ruta_apertura"
                    file_name.write("   </nombre>\n")

                elif re.search(pattern_ruta_nombre_contenido_post, i):
                    nombre2 = i.replace("\n", "")
                    nombre2 = nombre2.replace(" ", "")
                    nombre1 = re.findall(pattern_ruta_nombre_contenido_post, nombre2)[0]
                    file_name.write("       "+ nombre1 +"\n")
                    estado == "ruta_nombre_apertura"  

            elif estado == "ruta_inicio_apertura":
                if re.search(pattern_ruta_inicio_cerradura, i):
                    estado = "ruta_apertura"
                    file_name.write("   </inicio>\n")

                elif re.search(pattern_ruta_inicio_contenido_post, i):
                    inicio2 = i.replace("\n", "")
                    inicio2 = inicio2.replace(" ", "")
                    inicio1 = re.findall(pattern_ruta_inicio_contenido_post, inicio2)[0]
                    file_name.write("       "+ inicio1 +"\n")
                    estado == "ruta_inicio_apertura" 
            
            elif estado == "ruta_fin_apertura":
                if re.search(pattern_ruta_fin_cerradura, i):
                    estado = "ruta_apertura"
                    file_name.write("   </fin>\n")

                elif re.search(pattern_ruta_fin_contenido_post, i):
                    fin2 = i.replace("\n", "")
                    fin2 = fin2.replace(" ", "")
                    fin1 = re.findall(pattern_ruta_fin_contenido_post, fin2)[0]
                    file_name.write("       "+ fin1 +"\n")
                    estado == "ruta_fin_apertura"

            elif estado == "ruta_peso_apertura":
                if re.search(pattern_ruta_peso_cerradura, i):
                    estado = "ruta_apertura"
                    file_name.write("   </peso>\n")
            
                elif re.search(pattern_ruta_peso_contenido_post, i):
                    peso2 = i.replace("\n", "")
                    peso2 = peso2.replace(" ", "")
                    peso1 = re.findall(pattern_ruta_peso_contenido_post, peso2)[0]
                    file_name.write("       "+ peso1 +"\n")
                    estado == "ruta_peso_apertura"


            elif estado == "estacion_nombre_apertura":
                if re.search(pattern_estacion_nombre_cerradura, i):
                    estado = "estacion_apertura"
                    file_name.write("   </nombre>\n")
                
                elif re.search(pattern_estacion_nombre_contenido_post, i):
                    nombre2 = i.replace("\n", "")
                    nombre2 = nombre2.replace(" ", "")
                    nombre1 = re.findall(pattern_estacion_nombre_contenido_post, nombre2)[0]
                    file_name.write("       "+ nombre1 +"\n")
                    estado == "estacion_nombre_apertura"

            elif estado == "estacion_estado_apertura":
                if re.search(pattern_estacion_estado_cerradura, i):
                    estado = "estacion_apertura"
                    file_name.write("   </estado>\n")

                elif re.search(pattern_estacion_estado1_contenido_post, i):
                    estado2 = i.replace("\n", "")
                    estado2 = estado2.replace(" ", "")
                    estado1 = re.findall(pattern_estacion_estado1_contenido_post, estado2)[0]
                    file_name.write("       "+ estado1 +"\n")
                    estado == "estacion_estado_apertura"
                
                elif re.search(pattern_estacion_estado2_contenido_post, i):
                    estado2 = i.replace("\n", "")
                    estado2 = estado2.replace(" ", "")
                    estado1 = re.findall(pattern_estacion_estado2_contenido_post, estado2)[0]
                    file_name.write("       "+ estado1 +"\n")
                    estado == "estacion_estado_apertura"


            elif estado == "estacion_color_apertura":
                if re.search(pattern_estacion_color_cerradura, i):
                    estado = "estacion_apertura"
                    file_name.write("   </color>\n")
                
                elif re.search(pattern_estacion_color_contenido_post, i):
                    color2 = i.replace("\n", "")
                    color2 = color2.replace(" ", "")
                    color1 = re.findall(pattern_estacion_color_contenido_post, estado2)[0]
                    file_name.write("       "+ color1 +"\n")
                    estado == "estacion_color_apertura"
            
            
    file_name.close()
