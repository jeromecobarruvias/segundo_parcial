from ejercicios import ejercicio1_cine as ej1
from ejercicios import ejercicio2_combustible as ej2

def ejecutar_ejercicio1():
    print("Ejercicio 1: Pendiente")

def ejecutar_ejercicio2():
    print("Ejercicio 2: Pendiente")

def mostrar_menu():
    print("Seleccione un ejercicio para ejecutar:")
    print("1. Ejercicio 1: Cine")
    print("2. Ejercicio 2: Combustible")
    print("0. Salir")

def menu():
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Ingrese el número del ejercicio que desea ejecutar (o 0 para salir): ")

        if opcion == "1":
            ejecutar_ejercicio1()
        elif opcion == "2":
            ejecutar_ejercicio2()
        elif opcion == "0":
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Por favor, intente nuevamente.")