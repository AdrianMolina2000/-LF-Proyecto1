import re

def analizar_archivo(path):
    file_name = open("corregido.txt", "w")
    #Ruta
    pattern_ruta_apertura = r"<[^/]*[R|r][U|u][T|t][A|a](.)*>"
    pattern_ruta_nombre_apertura = r"<[^/]*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
    pattern_ruta_nombre_cerradura = r"</(.)*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
    pattern_ruta_inicio_apertura = r"<[^/]*[I|i][N|n][I|i][C|c][I|i][O|o](.)*>"
    pattern_ruta_inicio_cerradura = r"</(.)*[I|i][N|n][I|i][C|c][I|i][O|o](.)*>"
    pattern_ruta_fin_apertura = r"<[^/]*[F|f][I|i][N|n](.)*>"
    pattern_ruta_fin_cerradura = r"</(.)*[F|f][I|i][N|n](.)*>"
    pattern_ruta_peso_apertura = r"<[^/]*[P|p][E|e][S|s][O|o](.)*>"
    pattern_ruta_peso_cerradura = r"</(.)*[P|p][E|e][S|s][O|o](.)*>"
    pattern_ruta_cerradura = r"</(.)*[R|r][U|u][T|t][A|a](.)*>"

    pattern_estacion_apertura = r"<[^/]*[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n](.)*>"
    pattern_estacion_nombre_apertura = r"<[^/]*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
    pattern_estacion_nombre_cerradura = r"</(.)*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
    pattern_estacion_estado_apertura = r"<[^/]*[E|e][S|s][T|t][A|a][D|d][O|o](.)*>"
    pattern_estacion_estado_cerradura = r"</(.)*[E|e][S|s][T|t][A|a][D|d][O|o](.)*>"
    pattern_estacion_color_apertura = r"<[^/]*[C|c][O|o][L|l][O|o][R|r](.)*>"
    pattern_estacion_color_cerradura = r"</(.)*[C|c][O|o][L|l][O|o][R|r](.)*>"
    pattern_estacion_cerradura = r"</(.)*[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n](.)*>"
    
    pattern_nombre_apertura = r"<[^/]*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
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
                        estado = "nada"
                        file_name.write("<nombre>\n")
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
                        file_name.write("   </nombre>\n")
                    else:
                        estado = "ruta_nombre_apertura"
                        file_name.write("   <nombre>\n")
                
                elif re.search(pattern_ruta_inicio_apertura, i):
                    if re.search(pattern_ruta_inicio_cerradura, i):
                        estado = "ruta_apertura"
                        file_name.write("   <inicio>\n")
                        file_name.write("   </inicio>\n")
                    else:
                        estado = "ruta_inicio_apertura"
                        file_name.write("   <inicio>\n")
                
                elif re.search(pattern_ruta_fin_apertura, i):
                    if re.search(pattern_ruta_fin_cerradura, i):
                        estado = "ruta_apertura"
                        file_name.write("   <fin>\n")
                        file_name.write("   </fin>\n")
                    else:
                        estado = "ruta_fin_apertura"
                        file_name.write("   <fin>\n")
                        
                
                elif re.search(pattern_ruta_peso_apertura, i):
                    if re.search(pattern_ruta_peso_cerradura,i):
                        estado = "ruta_apertura"
                        file_name.write("   <peso>\n")
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
                        file_name.write("   </nombre>\n")

                    else:
                        estado = "estacion_nombre_apertura"
                        file_name.write("   <nombre>\n")
                
                elif re.search(pattern_estacion_estado_apertura, i):
                    if re.search(pattern_estacion_estado_cerradura, i):
                        estado = "estacion_apertura"
                        file_name.write("   <estado>\n")
                        file_name.write("   </estado>\n")

                    else:
                        estado = "estacion_estado_apertura"
                        file_name.write("   <estado>\n")
                
                elif re.search(pattern_estacion_color_apertura, i):
                    if re.search(pattern_estacion_color_cerradura, i):
                        estado = "estacion_apertura"
                        file_name.write("   <color>\n")
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




            #Nivel 2
            elif estado == "ruta_nombre_apertura":
                if re.search(pattern_ruta_nombre_cerradura, i):
                    estado = "ruta_apertura"
                    file_name.write("   </nombre>\n")

            elif estado == "ruta_inicio_apertura":
                if re.search(pattern_ruta_inicio_cerradura, i):
                    estado = "ruta_apertura"
                    file_name.write("   </inicio>\n")
            
            elif estado == "ruta_fin_apertura":
                if re.search(pattern_ruta_fin_cerradura, i):
                    estado = "ruta_apertura"
                    file_name.write("   </fin>\n")
            
            elif estado == "ruta_peso_apertura":
                if re.search(pattern_ruta_peso_cerradura, i):
                    estado = "ruta_apertura"
                    file_name.write("   </peso>\n")
            
            


            elif estado == "estacion_nombre_apertura":
                if re.search(pattern_estacion_nombre_cerradura, i):
                    estado = "estacion_apertura"
                    file_name.write("   </nombre>\n")

            elif estado == "estacion_estado_apertura":
                if re.search(pattern_estacion_estado_cerradura, i):
                    estado = "estacion_apertura"
                    file_name.write("   </estado>\n")
            
            elif estado == "estacion_color_apertura":
                if re.search(pattern_estacion_color_cerradura, i):
                    estado = "estacion_apertura"
                    file_name.write("   </color>\n")
            

            #Nivel 3



            
    file_name.close()


analizar_archivo("pa2.txt")