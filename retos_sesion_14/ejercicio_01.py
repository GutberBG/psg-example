def promedio_calificaciones(calificaciones):
    
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

calificaciones = [50, 75, 80, 91, 70]
resultado = promedio_calificaciones(calificaciones)
print(f"El promedio de las calificaciones es: {resultado:.2f}")