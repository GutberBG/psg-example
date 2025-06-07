cadena = input("Ingrese una cadena: ")
cadena_limpia = ''.join(cadena.split()).lower()
es_palindrome = cadena_limpia == cadena_limpia[::-1]
print(f"La cadena '{cadena}' es palindrome: {es_palindrome}")