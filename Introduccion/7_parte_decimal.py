# Escriba un programa que entregue la parte decimal de un
# número real ingresado por el usuario.

import math

num = float(input("Ingrese  un numero: "))

decimal = math.modf(num)

print(decimal)