"""Eval2 - Metodo de Falsa Posicion (Regula Falsi).

f(x) = (x-1)*(x-1)*(x+2) = x^3 - 3x + 2
Raices: x = 1 (doble) y x = -2.
En el intervalo [-3, 0] se localiza la raiz x = -2 (hay cambio de signo).

A diferencia de la biseccion (que toma el punto medio), la falsa posicion toma
p_n como el cero de la recta que une (a_n, f(a_n)) y (b_n, f(b_n)):

    p_n = (a_n * f(b_n) - b_n * f(a_n)) / (f(b_n) - f(a_n))
"""


def f(x):
    return (x - 1) * (x - 1) * (x + 2)


def falsa_posicion(a, b, tol=1e-6, max_iter=100):
    """Genera la sucesion {p_n} por falsa posicion en [a, b]."""
    if f(a) * f(b) >= 0:
        raise ValueError("No hay cambio de signo en [a, b]: f(a)*f(b) >= 0")

    print(f"{'n':>3} | {'a_n':>12} | {'b_n':>12} | {'p_n':>12} | {'f(p_n)':>14}")
    print("-" * 65)

    p_ant = None
    for n in range(1, max_iter + 1):
        fa, fb = f(a), f(b)
        # Cero de la recta secante que une (a, f(a)) y (b, f(b))
        p = (a * fb - b * fa) / (fb - fa)
        fp = f(p)
        print(f"{n:>3} | {a:>12.8f} | {b:>12.8f} | {p:>12.8f} | {fp:>14.2e}")

        # Criterios de parada: |f(p)| < tol  o  |p - p_ant| < tol
        if abs(fp) < tol or (p_ant is not None and abs(p - p_ant) < tol):
            return p, n

        # Elegir el subintervalo con cambio de signo
        if fa * fp < 0:
            b = p
        else:
            a = p
        p_ant = p

    return p, max_iter


if __name__ == "__main__":
    raiz, iteraciones = falsa_posicion(-3.0, 0.0, tol=1e-6)
    print("-" * 65)
    print(f"Raiz aproximada: {raiz:.8f}")
    print(f"f(raiz) = {f(raiz):.2e}")
    print(f"Iteraciones: {iteraciones}")
