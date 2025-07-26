numero1, numero2, operacion = input("Ingrese los números y la operación (ejemplo: 10, 5, +): ").split(", ")
numero1 = float(numero1)
numero2 = float(numero2)
operacion = operacion.strip()

if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    resultado = numero1 / numero2