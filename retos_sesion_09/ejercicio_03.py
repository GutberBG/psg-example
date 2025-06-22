personas = ["Ana", "José", "María", "Luis", "Pedro", "Carla", "Sofía", "Javier", "Lucía", "Miguel"]
sub_lista = personas[5:10:2]
existe_jose = "José" in personas
sub_lista.sort()
personas.sort(reverse=True)

print("Lista original:", personas)
print("Sub lista:", sub_lista)
print("¿Existe José?", existe_jose)
print("Sub lista ordenada:", sub_lista)
print("Lista original ordenada (z-a):", personas)