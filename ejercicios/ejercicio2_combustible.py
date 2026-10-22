'''
Un conductor necesita conocer el rendimiento de combustible de su vehículo y el costo de un recorrido. El 
usuario deberá proporcionar la distancia recorrida en kilómetros y la cantidad de litros consumidos. El 
precio por litro será de $24.00. 

'''

# PROBLEMA
# Calcular el importe de un recorrido en automóvil considerando la distancia recorrida y el consumo de combustible.

# ENTRADAS
# distancia : real, distancia recorrida en kilómetros, mayor o igual a 0.
# litros : real, cantidad de litros consumidos, mayor o igual a 0.

# SALIDAS
# importe : real, pesos mexicanos, formato de moneda con 2 decimales.
# rendimiento : real, kilómetros por litro, formato con 2 decimales.

# REGLAS Y SUPUESTOS
# - El precio por litro de combustible es de $24.00.
# - El rendimiento del vehículo se calcula como la distancia recorrida dividida entre la cantidad de litros consumidos.
# - Se debe calcular el costo total del recorrido.

# ALGORITMO
# 1. Leer la distancia recorrida y la cantidad de litros consumidos.
# 2. Calcular el rendimiento del vehículo: distancia / litros.
# 3. Calcular el costo del combustible: litros * 24.
# 4. Mostrar el costo total del recorrido.

# CASOS DE PRUEBA
# 120 km  10 litros consumidos 
# 250 km  20 litros consumidos
# 180 km  15 litros consumidos
# 300 km  25 litros consumidos

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerDatos() -> (distancia, litros) : leer y devolver la distancia y litros consumidos.
# calcularRendimiento(distancia, litros) -> rendimiento : calcular el rendimiento del vehículo en km/l.
# calcularImporte(distancia, litros) -> importe : calcular el importe total del recorrido.
# mostrarImporte(importe) -> None : mostrar el importe con 2 decimales.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

from tabulate import tabulate

def leerDatos():
    distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
    litros = float(input("Ingrese la cantidad de litros consumidos: "))
    return distancia, litros

def calcularRendimiento(distancia, litros):
    if litros > 0:
        return distancia / litros
    return 0

def calcularImporte(distancia, litros):
    precio_por_litro = 24.00
    return litros * precio_por_litro

def mostrarImporte(distancia, litros, rendimiento, importe):
    filas = [
        ["Kilometros recorridos", distancia],
        ["Litros consumidos", litros],
        ["Precio por litro", "$24.00"],
        ["Rendimiento del vehículo (km/l)", f"{rendimiento:.2f}"],
        ["Importe total del recorrido", f"${importe:.2f}"]
    ]

    print(tabulate(filas, headers=["Kilometros recorridos", "Litros consumidos", "Precio por litro", "Rendimiento del vehículo (km/l)", "Importe total del recorrido"], tablefmt="grid"))
