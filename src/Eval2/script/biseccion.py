"""Eval2 - Metodo de la Biseccion.

f(x) = (x-1)*(x-1)*(x+2) = x^3 - 3x + 2
Raices: x = 1 (doble) y x = -2.
En el intervalo [-3, 0] se localiza la raiz x = -2 (hay cambio de signo).
"""


def f(x):
    return (x - 1) * (x - 1) * (x + 2)


def biseccion(a, b, tol=1e-6, max_iter=100):
    """Genera la sucesion {p_n} por biseccion en [a, b]."""
    if f(a) * f(b) >= 0:
        raise ValueError("No hay cambio de signo en [a, b]: f(a)*f(b) >= 0")

    print(f"{'n':>3} | {'a_n':>12} | {'b_n':>12} | {'p_n':>12} | {'f(p_n)':>14}")
    print("-" * 65)

    p_ant = None
    for n in range(1, max_iter + 1):
        p = (a + b) / 2.0
        fp = f(p)
        print(f"{n:>3} | {a:>12.8f} | {b:>12.8f} | {p:>12.8f} | {fp:>14.2e}")

        # Criterios de parada: |f(p)| < tol  o  |p - p_ant| < tol
        if abs(fp) < tol or (p_ant is not None and abs(p - p_ant) < tol):
            return p, n

        # Elegir el subintervalo con cambio de signo
        if f(a) * fp < 0:
            b = p
        else:
            a = p
        p_ant = p

    return p, max_iter


if __name__ == "__main__":
    raiz, iteraciones = biseccion(-3.0, 0.0, tol=1e-6)
    print("-" * 65)
    print(f"Raiz aproximada: {raiz:.8f}")
    print(f"f(raiz) = {f(raiz):.2e}")
    print(f"Iteraciones: {iteraciones}")
