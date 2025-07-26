contactos = []
nombre = input("Ingrese el nombre del contacto: ")
telefono = input("Ingrese el número de teléfono del contacto: ")
if len(telefono) == 12 and telefono.startswith("+591") and nombre:
    contactos.append({"nombre": nombre, "telefono": telefono})
    print("Contacto guardado.")
else:
    print("Datos incorrectos.")
