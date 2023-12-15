# Escriba un programa que reciba como entrada las longitudes de los dos
# catetos a y b de un triángulo rectángulo, y que entregue como salida
# el largo de la hipotenusa c del triangulo, dado
# por el teorema de Pitágoras: C² = a² + b².

import math

cateto_a = int(input("Ingrese cateto a: "))
cateto_b = int(input("Ingrese cateto b: "))

oper = float(cateto_a**2 + cateto_b**2)
hipotenusa = math.sqrt(float(oper))

print("La hipotenusa es", hipotenusa)