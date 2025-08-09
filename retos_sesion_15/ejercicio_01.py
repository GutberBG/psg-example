def division(num1, num2):
    if num2 == 0:
        raise ValueError("No se puede dividir entre cero")
    return num1 / num2

def suma(num1, num2):
    return num1 + num2
def resta(num1, num2):
    return num1 - num2
def multiplicacion(num1, num2):
    return num1 * num2

numeros = []
while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1.lower() == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2.lower() == "salir":
            break
        num1 = float(num1)
        num2 = float(num2)
        operacion = input("Ingrese la operación (suma, resta, multiplicación, división): ").lower()
        if operacion == "suma":
            resultado = suma(num1, num2)
        elif operacion == "resta":
            resultado = resta(num1, num2)
        elif operacion == "multiplicación":
            resultado = multiplicacion(num1, num2)
        elif operacion == "división":
            resultado = division(num1, num2)
        else:
            print("Operación no válida")
            continue
        print("El resultado de la", operacion, "es:", resultado)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error inesperado:", e)
    else:
        print("Operación realizada con éxito")
    