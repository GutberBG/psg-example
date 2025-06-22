
productos = ["Oreo", "Chizitos", "Bon Bon Bum", "Paleta Payaso"]
precios = [10, 5, 3, 8]

productos.append("Chocoramo")
precios.append(12)
productos.append("Galleta María")
precios.append(6)

if "Bon Bon Bum" in productos:
    index = productos.index("Bon Bon Bum")
    productos.pop(index)
    precios.pop(index)

oreo_precio = precios[productos.index("Oreo")]
chizitos_precio = precios[productos.index("Chizitos")]

max_precio = max(precios)
min_precio = min(precios)
producto_caro = productos[precios.index(max_precio)]
producto_barato = productos[precios.index(min_precio)]

total_productos = len(productos)

total_precio = sum(precios)

productos_precios = list(zip(productos, precios))
productos_precios.sort(key=lambda x: x[1])  
productos, precios = zip(*productos_precios)

productos = []
precios = []

print("Productos:", productos)
print("Precios:", precios)
print("Precio Oreo:", oreo_precio)
print("Precio Chizitos:", chizitos_precio)
print("Producto más caro:", producto_caro)
print("Producto más barato:", producto_barato)
print("Total de productos:", total_productos)
print("Total precio:", total_precio)