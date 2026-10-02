"""Eval2 - Genera un CSV de la funcion f(x) = (x-1)*(x-1)*(x+2).

Evalua f(x) en el rango [-10, 10] con paso 0.2 y guarda el resultado en
src/Eval2/data/funcion_valores.csv con columnas: x, f(x).
"""

import csv
import os

import numpy as np

# Rutas relativas a este script (script/ -> Eval2/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EVAL2_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(EVAL2_DIR, "data")


def f(x):
    return (x - 1) * (x - 1) * (x + 2)


def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    # Paso 0.2 en [-10, 10]. Se incluye el extremo 10 sumando el paso al tope.
    xs = np.arange(-10, 10 + 0.2, 0.2)
    xs = np.round(xs, 1)  # evitar colas como -9.99999999 por punto flotante

    destino = os.path.join(DATA_DIR, "funcion_valores.csv")
    with open(destino, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["x", "f(x)"])
        for x in xs:
            escritor.writerow([f"{x:.1f}", f"{f(x):.6f}"])

    print(f"CSV generado en: {destino}")
    print(f"Filas de datos: {len(xs)}")


if __name__ == "__main__":
    main()
