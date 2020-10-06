import re, os

class Token:
    def __init__(self, lex, tok, f, c):
        self.lexema = lex
        self.token = tok
        self.fila = f
        self.columna = c

def report(tokis):
    file_name = open("Reporte/index_2.html", "w")

    file_name.write("<!DOCTYPE html>\n<html>\n<head>\n")
    file_name.write("   <meta charset='UTF-8'>\n")
    file_name.write("   <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css'>\n")
    file_name.write("</head>\n")
    file_name.write("<body class='container grey lighten-1'>\n")
    file_name.write("   <table class='highlight'>\n")
    file_name.write("       <thead>\n")
    file_name.write("           <tr>\n")
    file_name.write("               <th>No.</th>\n")
    file_name.write("               <th>Fila</th>\n")
    file_name.write("               <th>Columna</th>\n")
    file_name.write("               <th>Lexema</th>\n")
    file_name.write("               <th>Token</th>\n")
    file_name.write("           </tr>\n")
    file_name.write("       </thead>\n")
    file_name.write("       <tbody>\n")
    
    num = 1
    for toke in tokis:
        file_name.write("           <tr>\n")
        file_name.write(f"                <th><strong>{num}</strong></th>\n")
        file_name.write(f"                <th><strong>{toke.fila}</strong></th>\n")
        file_name.write(f"                <th><strong>{toke.columna}</strong></th>\n")
        file_name.write(f"                <th><strong>{toke.lexema}</strong></th>\n")
        file_name.write(f"                <th><strong>{toke.token}</strong></th>\n")
        file_name.write("           </tr>\n")
        num +=1

    file_name.write("       </tbody>\n")
    file_name.write("   </table>\n")
    file_name.write("</body>\n</html>\n")

    file_name.close()
    os.startfile("Reporte\index_2.html")

#PATRONES
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


    

def analizar_archivo_tokens(path):

    tokens = []

    
    with open(path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        n_linea = 1
        for linea in lineas:
            #RUTA
            if re.search(ruta_abierta, linea):
                obtener = re.sub("[<|>]", "", re.findall(ruta_abierta,linea)[0])
                tok = Token(obtener,"ruta", n_linea, re.search(ruta_abierta, linea).start()+1)
                tokens.append(tok)
            
            if re.search(ruta_cerrada, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(ruta_cerrada,linea)[0])
                tok = Token(obtener,"ruta", n_linea, re.search(ruta_cerrada, linea).start()+3)
                tokens.append(tok)
            #NOMBRE
            if re.search(nombre_abierta, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(nombre_abierta,linea)[0])
                tok = Token(obtener,"nombre", n_linea, re.search(nombre_abierta, linea).start()+2)
                tokens.append(tok)
            if re.search(nombre_cerrada, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(nombre_cerrada,linea)[0])
                tok = Token(obtener,"nombre", n_linea, re.search(nombre_cerrada, linea).start()+3)
                tokens.append(tok)
            #INICIO
            if re.search(inicio_abierta, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(inicio_abierta,linea)[0])
                tok = Token(obtener,"inicio", n_linea, re.search(inicio_abierta, linea).start()+2)
                tokens.append(tok)
            if re.search(inicio_cerrada, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(inicio_cerrada,linea)[0])
                tok = Token(obtener,"inicio", n_linea, re.search(inicio_cerrada, linea).start()+3)
                tokens.append(tok)
            #FIN
            if re.search(fin_abierta, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(fin_abierta,linea)[0])
                tok = Token(obtener,"fin", n_linea, re.search(fin_abierta, linea).start()+2)
                tokens.append(tok)
            if re.search(fin_cerrada, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(fin_cerrada,linea)[0])
                tok = Token(obtener,"fin", n_linea, re.search(fin_cerrada, linea).start()+3)
                tokens.append(tok)
            #PESO
            if re.search(peso_abierta, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(peso_abierta,linea)[0])
                tok = Token(obtener,"peso", n_linea, re.search(peso_abierta, linea).start()+2)
                tokens.append(tok)
            if re.search(peso_cerrada, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(peso_cerrada,linea)[0])
                tok = Token(obtener,"peso", n_linea, re.search(peso_cerrada, linea).start()+3)
                tokens.append(tok)
            #ESTACION
            if re.search(estacion_abierta, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(estacion_abierta,linea)[0])
                tok = Token(obtener,"estacion", n_linea, re.search(estacion_abierta, linea).start()+2)
                tokens.append(tok)
            if re.search(estacion_cerrada, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(estacion_cerrada,linea)[0])
                tok = Token(obtener,"estacion", n_linea, re.search(estacion_cerrada, linea).start()+3)
                tokens.append(tok)
            #ESTADO
            if re.search(estado_abierta, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(estado_abierta,linea)[0])
                tok = Token(obtener,"estado", n_linea, re.search(estado_abierta, linea).start()+2)
                tokens.append(tok)
            if re.search(estado_cerrada, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(estado_cerrada,linea)[0])
                tok = Token(obtener,"estado", n_linea, re.search(estado_cerrada, linea).start()+3)
                tokens.append(tok)
            #COLOR
            if re.search(color_abierta, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(color_abierta,linea)[0])
                tok = Token(obtener,"color", n_linea, re.search(color_abierta, linea).start()+2)
                tokens.append(tok)
            if re.search(color_cerrada, linea):
                obtener = re.sub("[<|>|/]", "", re.findall(color_cerrada,linea)[0])
                tok = Token(obtener,"color", n_linea, re.search(color_cerrada, linea).start()+3)
                tokens.append(tok)
            
            n_linea += 1
    report(tokens)

# analizar_archivo_tokens("input1.txt")