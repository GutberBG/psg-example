estudiantes = [('Miguel', 51), ('Daniel', 80), ('Virginia', 90), ('Franco', 40), ('Flabio', 30)]

for estudiante, nota in estudiantes:
    if nota >= 51:
        print(f"Felicitaciones {estudiante}, aprobaste el curso con una nota de {nota}.")
    else:
        print(f"{estudiante}, lamentablemente no aprobaste el curso con una nota de {nota}.")