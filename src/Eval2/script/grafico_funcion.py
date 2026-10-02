"""Eval2 - Grafico de la funcion f(x) = (x-1)*(x-1)*(x+2).

Dibuja la curva en el intervalo [-3, 0], marca el eje X y la raiz x = -2,
y guarda la imagen en src/Eval2/assets/funcion.png.
"""

import os

import matplotlib

matplotlib.use("Agg")  # backend sin ventana: guardar con savefig
import matplotlib.pyplot as plt
import numpy as np

# Rutas relativas a este script (script/ -> Eval2/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EVAL2_DIR = os.path.dirname(SCRIPT_DIR)
ASSETS_DIR = os.path.join(EVAL2_DIR, "assets")


def f(x):
    return (x - 1) * (x - 1) * (x + 2)


def main():
    os.makedirs(ASSETS_DIR, exist_ok=True)

    x = np.linspace(-3, 0, 400)
    y = f(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color="#1f77b4", linewidth=2, label="f(x) = (x-1)(x-1)(x+2)")
    plt.axhline(0, color="black", linewidth=0.8)          # eje X
    plt.axvline(0, color="black", linewidth=0.8)          # eje Y

    # Marcar la raiz x = -2 en el intervalo [-3, 0]
    plt.plot(-2, 0, "o", color="#d62728", markersize=9, label="Raiz x = -2")
    plt.annotate("x = -2", xy=(-2, 0), xytext=(-2.1, 3),
                 arrowprops=dict(arrowstyle="->", color="#d62728"))

    plt.title("Funcion f(x) = (x-1)(x-1)(x+2) en [-3, 0]")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    destino = os.path.join(ASSETS_DIR, "funcion.png")
    plt.savefig(destino, dpi=120)
    plt.close()
    print(f"Imagen generada en: {destino}")


if __name__ == "__main__":
    main()
