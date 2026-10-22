'''
Un cine necesita desarrollar un programa que permita determinar el importe de una compra de boletos. 
Cada boleto cuesta $75.00. El usuario deberá indicar cuántos boletos desea comprar. Cuando se adquieran 4 
boletos o más, se aplicará un descuento del 10% sobre el subtotal. Para compras menores a 4 boletos, no se 
aplicará descuento. 

'''

# PROBLEMA
# Calcular el importe de una compra de boletos de cine considerando el precio por boleto y el descuento correspondiente.

# ENTRADAS
# boletos : entero, cantidad de boletos a comprar, mayor o igual a 0.

# SALIDAS
# importe : real, pesos mexicanos, formato de moneda con 2 decimales.

# REGLAS Y SUPUESTOS
# - El precio por boleto es de $75.00.
# - Si se compran 4 boletos o más, se aplica un descuento del  10% sobre el subtotal.
# - Si se compran menos de 4 boletos, no se aplica descuento.

# ALGORITMO
# 1. Leer la cantidad de boletos a comprar.
# 2. Calcular el importe inicial: boletos * 75.
# 3. Si boletos >= 4:
#       importe = importe inicial * 0.90
# 4. En caso contrario:
#       importe = importe inicial
# 5. Calcular el descuento si aplica 
# 6. Mostrar el importe de la compra.

# CASOS DE PRUEBA
# 1
# 3
# 4
# 6

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerBoletos() -> boletos : leer y devolver la cantidad de boletos a comprar.
# calcularImporte(boletos) -> importe : calcular el importe total de la compra.
# calcularDescuento(boletos, importe) -> descuento : calcular el descuento aplicable según la cantidad de boletos.
# mostrarImporte(importe) -> None : mostrar el importe con 2 decimales.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

from tabulate import tabulate

def leerBoletos():
    boletos = int(input("Ingrese la cantidad de boletos a comprar: "))
    return boletos

def calcularImporte(boletos):
    precio_por_boleto = 75.00
    Importe = boletos * precio_por_boleto
    if boletos >= 4:
        Importe *= 0.90  # Aplicar descuento del 10%
    return Importe

def calcularDescuento(boletos, Importe):
    if boletos >= 4:
        return Importe * 0.10  # Descuento del 10%
    return 0

def mostrarImporte(boletos, Importe):
    filas = [
        ["Cantidad de boletos", f"{boletos}"],
        ["Precio por boleto", "$75.00"],
        ["Subtotal", f"${Importe:.2f}"],
        ["Descuento aplicado", "10%" if boletos >= 4 else "0%"],
        ["Importe total de la compra", f"${Importe - calcularDescuento(boletos, Importe):.2f}"]
    ]

    print(tabulate(filas, headers=["Cantidad de boletos", "Precio por boleto", "Importe", "Subtotal", "Descuento aplicado", "Importe total de la compra"], tablefmt="grid"))
