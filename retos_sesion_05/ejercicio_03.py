segundos = 1000000

semanas = segundos // 604800
dias = (segundos % 604800) // 86400
horas = (segundos % 86400) // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(segundos, "segundos = ", semanas, "semanas,", dias, "dias,", horas, "horas,", minutos, "minutos, ", segundos_restantes, "segundos")