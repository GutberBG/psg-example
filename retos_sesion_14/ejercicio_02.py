def calcular(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero"
num1 = 10
num2 = 5
operacion = "+"
resultado = calcular(num1, num2, operacion)
print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")