"""Pruebas del historial; listar devuelve copia para proteger el estado interno."""

import unittest

from historial import agregar, listar, limpiar


class PruebasHistorial(unittest.TestCase):
    def test_orden_reciente_primero_y_copia(self):
        historial = ["1 + 1 = 2", "2 + 2 = 4"]
        resultado = listar(historial)
        self.assertEqual(resultado, ["2 + 2 = 4", "1 + 1 = 2"])
        resultado.append("cambio externo")
        self.assertEqual(len(historial), 2)

    def test_limite_de_cinco(self):
        historial = []
        for numero in range(7):
            agregar(historial, str(numero))
        self.assertEqual(historial, ["2", "3", "4", "5", "6"])

    def test_limpiar_vacia_lista_original(self):
        historial = ["1 + 1 = 2"]
        limpiar(historial)
        self.assertEqual(historial, [])


if __name__ == "__main__":
    unittest.main()
