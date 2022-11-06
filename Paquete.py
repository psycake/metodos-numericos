from Programa_1 import *
from Programa_2 import *
from utilidades import *


def menu_principal():
    opciones_programas = {
        1: "Solución de Ecuaciones",
        2: "Solución de Matrices",

        0: "Salir del programa"
    }

    while True:
        clear_screen()
        print("Programas disponibles:\n")
        for opcion in opciones_programas.keys():
            print(f"{opcion} --- {opciones_programas[opcion]}")

        while True:
            try:
                eleccion = int(input("\n¿Qué procedimiento desea utilizar? "))
            except:
                print("\nIntroduzca un número entero.")
                continue

            if (eleccion >= 0) and (eleccion < len(opciones_programas.keys())):
                break
            else:
                print(
                    f"\nIntroduzca un número entre 0 y {len(opciones_programas.keys())-1}.")

        if eleccion == 1:
            menu_metodos()
        elif eleccion == 2:
            matrices()
        elif eleccion == 0:
            break


if __name__ == "__main__":
    portada("Paquete de Programas")
    menu_principal()
