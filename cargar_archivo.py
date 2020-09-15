import re, os

def convertir_cadena(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
        linea = ""
        for i in lineas:
            linea += i.replace("\n", "")
            linea = linea.replace(" ", "")
        return linea



def leer_archivo():
    ruta = input("Ingrese la ruta del archivo: ")
    if os.path.exists(ruta): 
        if re.search("\.txt", ruta):
            f = open(ruta , "r")
            print("==========================================\n\n")
            for linea in f:
                if "\n" in linea:
                    linea.replace("\n","")
                else: 
                    continue
                print(linea)
                
        
            print("------------------------------------------------------\n\n")
            var = input("Ingrese Enter para continuar: ")
            print("Regresando a menu principal...")
            print("\n\n------------------------------------------------------\n\n")
            f.close()
        else:
            print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("////Error -> Unicamente archivos .txt ////")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

    else:
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("/////  Error -> Ruta no encontrada  /////")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")



