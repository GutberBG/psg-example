def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
n = 5
resultado = lucas(n)
print(f"El {n}-ésimo número de la serie de Lucas es: {resultado}")