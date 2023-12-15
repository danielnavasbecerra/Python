# Escriba un programa que convierta de centímetros a pulgadas.
# Una pulgada es igual a 2.54 centímetros.

longitud = int(input("Ingrese longitud (cm): "))
conver = float(longitud / 2.54)

print(longitud, "cm =", round(conver, 4), "in")