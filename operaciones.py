"""Operaciones matemáticas básicas de la calculadora."""

import math


def calcular(operacion, a, b=None):
    """Calcula una operación; por ejemplo, calcular('+', 2, 3) devuelve 5."""
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
        try:
            return a ** b
        except (OverflowError, ZeroDivisionError) as exc:
            raise ValueError("El resultado de la potencia no es válido.") from exc
    if operacion == "raiz":
        if a < 0:
            raise ValueError("No existe una raíz cuadrada real de un número negativo.")
        return math.sqrt(a)
    raise ValueError(f"Operación no válida: {operacion!r}.")
