from ejercicios import ejercicio1_cine as ej1
from ejercicios import ejercicio2_combustible as ej2

def ejecutar_ejercicio1():
    boletos = ej1.leerBoletos()
    importe = ej1.calcularImporte(boletos)
    descuento = ej1.calcularDescuento(boletos, importe)
    importe_final = importe - descuento
    ej1.mostrarImporte(boletos, importe_final)

def ejecutar_ejercicio2():
    distancia, litros = ej2.leerDatos()
    rendimiento = ej2.calcularRendimiento(distancia, litros)
    importe = ej2.calcularImporte(distancia, litros)
    ej2.mostrarImporte(distancia, litros, rendimiento, importe)

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