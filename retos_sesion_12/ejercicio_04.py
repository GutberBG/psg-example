
edad = int(input("Ingrese su edad: "))
compra = float(input("Ingrese el monto de su compra: "))
if edad > 60 and compra > 1000:
    descuento = 0.2
elif 18 <= edad <= 60 and compra > 500:
    descuento = 0.1
else:
    descuento = 0.02
monto_descuento = compra * descuento
print(f"El monto de su descuento es: {monto_descuento}")
