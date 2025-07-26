numero = int(input("Ingrese un número (0 para salir): "))
while numero != 0:
    if numero % 7 == 0:
        print(f"{numero} es múltiplo de 7.")
    else:
        print(f"{numero} no es múltiplo de 7.")
    numero = int(input("Ingrese otro número (0 para salir): "))