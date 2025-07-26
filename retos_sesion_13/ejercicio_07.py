for numero in range(1, 101):
    if numero % 5 == 0 and numero % 7 == 0:
        print("FizzBuzz")
    elif numero % 5 == 0:
        print("Fizz")
    elif numero % 7 == 0:
        print("Buzz")
    else:
        print(numero)