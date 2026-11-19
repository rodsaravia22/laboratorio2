# Calculadora gráfica

Calculadora de escritorio hecha con Python y la biblioteca estándar. Incluye suma, resta, multiplicación, división, potencia y raíz cuadrada. El historial conserva las cinco operaciones correctas más recientes mientras la aplicación está abierta.

## Requisitos

- Python 3
- Tkinter disponible en la instalación de Python

## Ejecutar

Desde la carpeta del proyecto:

```bash
python main.py
```

En Windows también puedes usar `py -3 main.py`. Para probar la ventana con funciones temporales, ejecuta `python demo_interfaz.py`.

## Pruebas

```bash
python -m unittest discover -v
```

En Windows: `py -3 -m unittest discover -v`.

Las pruebas de `operaciones.py` muestran ejemplos sencillos de cada cálculo y verifican los errores esperados. Las de `historial.py` verifican el orden, el límite y el borrado. `listar` devuelve una copia para que un consumidor pueda modificar el resultado sin alterar la lista original.

## Gitflow

Usa una rama por módulo y fusiona las funcionalidades terminadas en `develop`; publica una versión mediante una rama `release` y una fusión final a `main`.

```bash
git flow init
git checkout develop
git flow feature start operaciones
git add operaciones.py test_operaciones.py
git commit -m "feat: implementar operaciones matemáticas"
git flow feature finish operaciones

git flow feature start historial
git add historial.py test_historial.py
git commit -m "feat: implementar historial de cálculos"
git flow feature finish historial

git flow feature start interfaz
git add main.py interfaz.py demo_interfaz.py README.md
git commit -m "feat: añadir interfaz gráfica"
git flow feature finish interfaz

git flow release start 1.0.0
git flow release finish 1.0.0
```
