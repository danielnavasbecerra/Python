# Escriba un programa que calcule el promedio de 4 notas
# ingresadas por el usuario:

n1 = int(input("Primera nota: "))
n2 = int(input("Segunda nota: "))
n3 = int(input("Tercera nota: "))
n4 = int(input("Cuarta nota: "))

prom = (n1 + n2 + n3 + n4) / 4
print("El promedio es: ", round(prom, 2))