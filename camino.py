import re 
prueba= "<estado>disponible</estado>"
pattern = r">[D|d][I|i][S|s][P|p][O|o][N|n][I|i][B|b][L|l][E|e]<"

nombre = re.findall(pattern, prueba)
print(nombre)
