# Escriba un programa que reciba como entrada el radio
# de un círculo y entregue como salida su perímetro y su área:

import math

radio = float(input("Ingrese el radio: "))
perimetro = 2 * math.pi * radio
area = math.pi * radio**2

print("Perimetro: ", round(perimetro, 1))
print("Área: ", round(area, 1))