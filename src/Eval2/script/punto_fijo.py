"""Eval2 - Metodo de iteracion de Punto Fijo.

Partimos de f(x) = (x-1)*(x-1)*(x+2) = x^3 - 3x + 2.
Reescribimos la ecuacion f(x) = 0 en la forma f(x) = x - g(x), con:

    g(x) = x^3 - 2x + 2

En efecto:  x - g(x) = x - (x^3 - 2x + 2) = -(x^3 - 3x + 2) = -f(x),
por lo tanto  f(x) = 0  <=>  x = g(x), y un punto fijo de g es una raiz de f.

Algoritmo de punto fijo:  p_n = g(p_{n-1}),  con p0 dado.

Nota de convergencia (Teorema de punto fijo): el metodo converge solo si
|g'(x)| <= k < 1 en el entorno de la raiz. Aqui g'(x) = 3x^2 - 2, de modo que
cerca de x = -2 se tiene |g'(-2)| = 10 > 1: con esta g el metodo DIVERGE
(salvo que se parta exactamente del punto fijo). El script lo deja en evidencia.
"""
import numpy as np

def f(x):
    return (x - 1) * (x - 1) * (x + 2)

# x**3 = 3x − 2   →   x = (3x − 2)^(1/3)   →   g(x) = (3x − 2) ** (1/3)
def g(x):
    v = 3 * x - 2
    return np.sign(v) * np.abs(v) ** (1 / 3)   # raiz cubica valida para v < 0


def g1(x):
    return x ** 3 - 2 * x + 2


def punto_fijo(p0, tol=1e-6, max_iter=50):
    """Genera la sucesion p_n = g(p_{n-1})."""
    print(f"{'n':>3} | {'x_n':>16} | {'g(x_n)':>16} | {'|x_n+1 - x_n|':>15}")
    print("-" * 60)

    p = p0
    for n in range(1, max_iter + 1):
        p_sig = g(p)
        print(f"{n:>3} | {p:>16.8f} | {p_sig:>16.8f} | {abs(p_sig - p):>15.2e}")

        if abs(p_sig - p) < tol:
            return p_sig, n

        # Si la sucesion diverge, cortamos para no desbordar
        if abs(p_sig) > 1e12:
            print("La sucesion diverge (|x_n| crece sin control).")
            return p_sig, n

        p = p_sig

    return p, max_iter


if __name__ == "__main__":
    # Aproximacion inicial dentro de [-3, 0]
    p0 = -1.5
    raiz, iteraciones = punto_fijo(p0, tol=1e-6)
    print("-" * 60)
    print(f"Aproximacion inicial p0 = {p0}")
    print(f"Ultimo valor: {raiz:.8f}")
    print(f"f(ultimo) = {f(raiz):.2e}")
    print(f"Iteraciones: {iteraciones}")
