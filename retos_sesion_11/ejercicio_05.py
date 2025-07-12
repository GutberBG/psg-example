arca = {
    "🐶": 2,
    "🐱": 2,
    "🐯": 2,
    "🐵": 2,
    "🦄": 0,
    "🦒": 1
}

arca.update({
    "🐘": 2,
    "🐍": 2,
    "🐲": 1
})
print(arca)

animales_en_arca = []
for especie, cantidad in arca.items():
    for _ in range(cantidad):
        animales_en_arca.append(especie)
print("Animales en el arca:", animales_en_arca)

existe_dragon = '🐲' in arca
print(existe_dragon)

if '🦄' in arca:
    del arca['🦄']
print("Arca después de eliminar unicornio:", arca)

if '🦒' in arca:
    arca['🦒'] = 2
print("Arca después de modificar jirafa:", arca)

arca.clear()
print(arca)