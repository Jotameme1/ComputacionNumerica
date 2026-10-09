"""Eval1: lectura del CSV del dolar observado y generacion de 3 graficos.

Lee src/Eval1/data/dolar_observado_sii_2022_2025.csv y guarda en
src/Eval1/assets:
  1. Curva del dolar_observado_promedio_clp por anio-mes.
  2. Diferencia mes a mes del dolar_observado_promedio_clp.
  3. Grafico de caja (boxplot) del dolar_observado_promedio_clp.
"""

import csv
import os

import matplotlib

matplotlib.use("Agg")  # backend sin ventana: guardar con savefig
import matplotlib.pyplot as plt
import numpy as np

# Rutas relativas a este script (script/ -> Eval1/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EVAL1_DIR = os.path.dirname(SCRIPT_DIR)
CSV_PATH = os.path.join(EVAL1_DIR, "data", "dolar_observado_sii_2022_2025.csv")
ASSETS_DIR = os.path.join(EVAL1_DIR, "assets")


def leer_csv(ruta):
    """Devuelve listas paralelas: etiquetas (anio-mes) y valores (float)."""
    etiquetas = []
    valores = []
    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            etiquetas.append(f"{fila['anio']}-{int(fila['mes_num']):02d}")
            valores.append(float(fila["dolar_observado_promedio_clp"]))
    return etiquetas, np.array(valores)


def grafico_curva(etiquetas, valores, destino):
    plt.figure(figsize=(14, 6))
    plt.plot(etiquetas, valores, marker="o", color="#1f77b4")
    plt.title("Dolar observado promedio (CLP) por anio-mes")
    plt.xlabel("Anio-Mes")
    plt.ylabel("Dolar observado promedio (CLP)")
    plt.xticks(rotation=90)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(destino, dpi=120)
    plt.close()


def grafico_diferencia(etiquetas, valores, destino):
    diferencias = np.diff(valores)  # valor[i] - valor[i-1]
    etiquetas_dif = etiquetas[1:]
    colores = ["#2ca02c" if d >= 0 else "#d62728" for d in diferencias]

    plt.figure(figsize=(14, 6))
    plt.bar(etiquetas_dif, diferencias, color=colores)
    plt.axhline(0, color="black", linewidth=0.8)
    plt.title("Diferencia mes a mes del dolar observado promedio (CLP)")
    plt.xlabel("Anio-Mes")
    plt.ylabel("Diferencia respecto al mes anterior (CLP)")
    plt.xticks(rotation=90)
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(destino, dpi=120)
    plt.close()


def grafico_caja(valores, destino):
    plt.figure(figsize=(6, 7))
    plt.boxplot(valores, orientation="vertical", patch_artist=True,
                boxprops=dict(facecolor="#aec7e8", color="#1f77b4"),
                medianprops=dict(color="#d62728"))
    plt.title("Distribucion del dolar observado promedio (CLP)")
    plt.ylabel("Dolar observado promedio (CLP)")
    plt.xticks([1], ["2022-2025"])
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(destino, dpi=120)
    plt.close()


def main():
    os.makedirs(ASSETS_DIR, exist_ok=True)
    etiquetas, valores = leer_csv(CSV_PATH)

    grafico_curva(etiquetas, valores, os.path.join(ASSETS_DIR, "01_curva_dolar.png"))
    grafico_diferencia(etiquetas, valores, os.path.join(ASSETS_DIR, "02_diferencia_mensual.png"))
    grafico_caja(valores, os.path.join(ASSETS_DIR, "03_boxplot_dolar.png"))

    print(f"Graficos generados en: {ASSETS_DIR}")


if __name__ == "__main__":
    main()
