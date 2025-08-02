def contar_vocales(cadena):
    """
    Cuenta la cantidad de vocales en una cadena.
    """
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador
cadena = "Python"
resultado = contar_vocales(cadena)
print(f"La cantidad de vocales en la cadena es: {resultado}")