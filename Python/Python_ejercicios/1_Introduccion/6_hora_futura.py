# Escriba un programa que pregunte al usuario la hora actual t del
# reloj y un número entero de horas h, que indique qué hora marcará
# el reloj dentro de h horas:

t = int(input("Hora actual: "))
h = int(input("Cantidad de horas: "))

hora_futura = (t + h) % 24

print("En", h, "horas, el reloj marcara las", hora_futura)