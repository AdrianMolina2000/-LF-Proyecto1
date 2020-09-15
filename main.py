import os
from cargar_archivo import leer_archivo

def datos_del_estudiante():
    print("\n==========================================")
    print("Adrian Samuel Molina Cabrera \n201903850")
    print("==========================================\n\n")



def opciones_del_menu():
    print("1. Cargar Archivo")
    print("2. Graficar Ruta")
    print("3. Graficar Mapa")
    print("4. Salir\n")


def menu_principal():
    while True:
        opciones_del_menu() 
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion in range(5):

                if opcion == 1:
                    print("Ha marcado la opcion Cargar Archivo")
                    print("==========================================\n")
                    leer_archivo()

                
                elif opcion == 2:
                    print("Ha marcado la opcion Graficar Ruta")
                    print("==========================================\n")
                elif opcion == 3:
                    print("Ha marcado la opcion Graficar Mapa")
                    print("==========================================\n")
                elif opcion == 4:
                    print("Saliendo...\n")
                    break
            else:
                print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("/////Error -> ingrese numeros del 1 al 3/////")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        except ValueError:

            print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("/////Error -> ingrese datos nuevamente/////") 
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")


    

if __name__ == "__main__":
    datos_del_estudiante()
    try:
        menu_principal()
    except:
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("///// Error -> Error -> Error ->  Error /////") 
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        
        menu_principal()