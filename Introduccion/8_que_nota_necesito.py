# Un alumno desea saber que nota necesita en el tercer certamen
# para aprobar un ramo.

# Donde **NC** es el promedio de certámenes, **NL** el promedio
# de laboratorio y **NF** la nota final.

# Escriba un programa que pregunte al usuario las notas de los
# dos primeros certamen y la nota de laboratorio, y muestre
# la nota que necesita el alumno para aprobar el ramo con nota
# final 60.


# Pide al usuario ingresar notas
certamen_1 = int(input("Ingrese nota Certamen 1: "))
certamen_2 = int(input("Ingrese nota Certamen 2: "))
Nl = int(input("Ingrese nota Laboratorio: "))

# Formula para hallar la nota necesaria en certamen 3
NC = (59.5 - 0.3 * Nl) / 0.7
certamen_3 = 3 * NC - (certamen_1 + certamen_2) + 1

# Imprime la nota necesaria para aprobar
print("Nesesita nota", int(round(certamen_3)), "en el certamen 3")