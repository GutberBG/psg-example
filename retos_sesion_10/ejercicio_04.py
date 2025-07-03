jane_postres = ["Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"]
jhon_postres = ["Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"]

jane_set = set(jane_postres)
jhon_set = set(jhon_postres)

postres_comunes = jane_set.intersection(jhon_set)

porcentaje_comun = (len(postres_comunes) / len(jane_set)) * 100

if porcentaje_comun > 50:
    print("son compatibles")
else:
    print("no son compatibles")