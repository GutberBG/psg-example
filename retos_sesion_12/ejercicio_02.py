
usuarios = {
    'admin': 'admin123',
    'user1': 'user123',
    'user2': 'user123',
    'user3': 'user123'
}
usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")
if usuario in usuarios and usuarios[usuario] == contraseña:
    print(f"Acceso Aprobado")
else:
    print("Acceso Denegado")

