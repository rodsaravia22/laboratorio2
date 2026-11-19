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

## Flujo de trabajo Gitflow

La rama estable es `main`; el trabajo de integración se realiza en `develop`. Cada integrante debe actualizar `develop`, crear su propia rama y abrir un pull request hacia `develop`. No se integra trabajo directamente en `main`.

```bash
git clone git@github.com:rodsaravia22/laboratorio2.git
cd laboratorio2
git switch develop
git pull --ff-only origin develop
git switch -c feature/operaciones  # o feature/historial, feature/interfaz
```

Después de hacer cambios y revisarlos:

```bash
git status
git add operaciones.py test_operaciones.py  # sustituye por los archivos de tu módulo
git diff --staged
git commit -m "Implementar y probar operaciones"
git push -u origin feature/operaciones
```

Abre un pull request de `feature/operaciones` hacia `develop`. El equipo revisa los cambios y ejecuta `python -m unittest discover -v` y `python main.py` tras integrarlos.

Cuando el equipo apruebe la integración, prepara la publicación:

```bash
git switch develop
git pull --ff-only origin develop
git switch -c release/1.0.0
python -m unittest discover -v
```

Abre un pull request de `release/1.0.0` a `main` y otro de `release/1.0.0` a `develop`. Después de su revisión e integración, etiqueta la versión:

```bash
git switch main
git pull --ff-only origin main
git tag -a v1.0.0 -m "Calculadora grafica 1.0.0"
git push origin v1.0.0
```
