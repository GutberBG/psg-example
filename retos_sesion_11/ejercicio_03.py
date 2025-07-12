especies_animales = {
    'canino': '🐶',
    'felino': '🐱',
    'aves': ['🐦', '🦅']
}

aves = especies_animales.pop('aves', None)
print(aves)
print(especies_animales)

especies_animales['felino'] = '🐈'
print(especies_animales)

especies_animales['caninos'] = ['🐶', '🐕']
del especies_animales['canino']
print(especies_animales)

    