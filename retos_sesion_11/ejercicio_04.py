habitats_en_peligro = {
    "polo_norte": {
        "especies": {"oso polar", "morsa", "ballena"},
        "amenazas": ["cambio climático", "derretimiento de hielo"]
    },
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"},
        "amenazas": ["deforestación", "caza furtiva"]
    }
}

habitats_en_peligro.update({
    "sabana_africana": {
        "especies": {"elefante", "jirafa"},
        "amenazas": ["caza furtiva", "pérdida de hábitat"]
    },
    "arrecife_de_corales": {
        "especies": {"tortuga marina", "pez payaso"},
        "amenazas": ["contaminación", "blanqueamiento"]
    }
})
print(habitats_en_peligro)

existe_amazonas = 'amazonas' in habitats_en_peligro
print(f"¿Existe el hábitat 'amazonas'? {'Sí' if existe_amazonas else 'No'}")
habitats_en_peligro['amazonas']['especies'].add('anaconda')
print(f"Especies en el hábitat 'amazonas': {habitats_en_peligro['amazonas']['especies']}")
print(habitats_en_peligro)
