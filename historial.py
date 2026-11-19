"""Operaciones para mantener el historial de cálculos en memoria."""


def agregar(historial, texto):
    """Añade una operación correcta y conserva solo las cinco más recientes."""
    historial.append(texto)
    del historial[:-5]


def listar(historial):
    """Devuelve una copia en orden reciente; modificarla no altera el original."""
    return list(reversed(historial))


def limpiar(historial):
    """Vacía la lista original para que todos sus usuarios vean el cambio."""
    historial.clear()
