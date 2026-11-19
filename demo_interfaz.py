"""Ejecuta la ventana de forma independiente con funciones temporales."""

import math

from interfaz import iniciar_interfaz


def calcular(operacion, a, b=None):
    if operacion == "+":
        return a + b
    if operacion == "-":
        return a - b
    if operacion == "*":
        return a * b
    if operacion == "/":
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b
    if operacion == "**":
        if a == 0 and b < 0:
            raise ValueError("Cero no puede elevarse a un exponente negativo.")
        return a ** b
    if operacion == "raiz":
        if a < 0:
            raise ValueError("No existe una raíz real para un número negativo.")
        return math.sqrt(a)
    raise ValueError("Operación no válida.")


def agregar(historial, texto):
    historial.append(texto)
    del historial[:-5]


def listar(historial):
    return list(reversed(historial))


def limpiar(historial):
    historial.clear()


if __name__ == "__main__":
    iniciar_interfaz(calcular, agregar, listar, limpiar)
