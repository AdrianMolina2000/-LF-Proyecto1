import re

pattern = r"<[R|r][U|u][T|t][A|a]>"
texto = "<RuTa><ruTa><Ruta><ruta><ruta>"

if re.search(pattern, texto):
    print(re.findall(pattern, texto))

