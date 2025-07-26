while True:
    frase = input("Ingrese una frase (o 'salir' para terminar): ")
    if frase.lower() == 'salir':
        print("Saliendo del programa.")
        break
    frase_sin_espacios = ''.join(frase.split()).lower()
    if frase_sin_espacios == frase_sin_espacios[::-1]:
        print("La frase es un palíndromo.")
    else:
        print("La frase no es un palíndromo.")