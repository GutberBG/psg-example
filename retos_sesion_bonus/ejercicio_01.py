frutas = ['🍅','🍇','🍈','🍉','🍊','🍌','🍍','🍌','🍊','🍉','🍈','🍇','🍅','🍅','🍇']

def contar_frutas(lista_frutas):
    contador = {}
    for fruta in lista_frutas:
        if fruta in contador:
            contador[fruta] += 1
        else:
            contador[fruta] = 1
    return contador

def imprimir_conteo(conteo):
    for fruta, cantidad in conteo.items():
        if cantidad == 1:
            print(f"Hay {cantidad} {fruta}.")
        else:
            print(f"Hay {cantidad} {fruta}s.")

conteo_frutas = contar_frutas(frutas)
imprimir_conteo(conteo_frutas)
