"""Eval2 - Metodo de la Secante.

f(x) = (x-1)*(x-1)*(x+2) = x^3 - 3x + 2
Raices: x = 1 (doble) y x = -2.
Se parte de dos aproximaciones iniciales p0, p1 en el intervalo [-3, 0].

Formula:
    p_n = p_{n-1} - f(p_{n-1}) * (p_{n-1} - p_{n-2}) / (f(p_{n-1}) - f(p_{n-2}))
"""


def f(x):
    return (x - 1) * (x - 1) * (x + 2)


def secante(p0, p1, tol=1e-6, max_iter=100):
    """Genera la sucesion {p_n} por el metodo de la secante."""
    print(f"{'n':>3} | {'p_n':>14} | {'f(p_n)':>14} | {'|p_n - p_n-1|':>15}")
    print("-" * 56)
    print(f"{0:>3} | {p0:>14.8f} | {f(p0):>14.2e} | {'':>15}")
    print(f"{1:>3} | {p1:>14.8f} | {f(p1):>14.2e} | {abs(p1 - p0):>15.2e}")

    for n in range(2, max_iter + 1):
        f0, f1 = f(p0), f(p1)
        if f1 - f0 == 0:
            raise ZeroDivisionError("f(p_n-1) - f(p_n-2) = 0: division por cero")

        p = p1 - f1 * (p1 - p0) / (f1 - f0)
        print(f"{n:>3} | {p:>14.8f} | {f(p):>14.2e} | {abs(p - p1):>15.2e}")

        if abs(p - p1) < tol or abs(f(p)) < tol:
            return p, n

        p0, p1 = p1, p

    return p, max_iter


if __name__ == "__main__":
    # Dos aproximaciones iniciales dentro de [-3, 0]
    raiz, iteraciones = secante(-3.0, 0.0, tol=1e-6)
    print("-" * 56)
    print(f"Raiz aproximada: {raiz:.8f}")
    print(f"f(raiz) = {f(raiz):.2e}")
    print(f"Iteraciones: {iteraciones}")
