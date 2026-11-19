"""Ejemplos ejecutables: sumar 2 y 3 da 5; la raíz de 9 da 3."""

import unittest

from operaciones import calcular


class PruebasOperaciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calcular("+", 2, 3), 5)

    def test_resta(self):
        self.assertEqual(calcular("-", 7, 2), 5)

    def test_multiplicacion(self):
        self.assertEqual(calcular("*", 4, 3), 12)

    def test_division(self):
        self.assertEqual(calcular("/", 9, 3), 3)

    def test_potencia(self):
        self.assertEqual(calcular("**", 2, 3), 8)

    def test_raiz(self):
        self.assertEqual(calcular("raiz", 9), 3)

    def test_operacion_invalida(self):
        with self.assertRaises(ValueError):
            calcular("%", 4, 2)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            calcular("/", 4, 0)

    def test_cero_a_exponente_negativo(self):
        with self.assertRaises(ValueError):
            calcular("**", 0, -1)

    def test_raiz_negativa(self):
        with self.assertRaises(ValueError):
            calcular("raiz", -1)


if __name__ == "__main__":
    unittest.main()
