tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

conjunto_fisica = set(tienda_fisica)
conjunto_online = set(tienda_online)

compraron_en_ambos = conjunto_fisica.intersection(conjunto_online)
print("Compraron en ambos canales:", compraron_en_ambos)

compraron_solo_fisica = conjunto_fisica.difference(conjunto_online)
print("Compraron solo en la tienda física:", compraron_solo_fisica)

compraron_solo_online = conjunto_online.difference(conjunto_fisica)
print("Compraron solo online:", compraron_solo_online)
