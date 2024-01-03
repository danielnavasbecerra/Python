# Escriba un programa que pida al usuario dos palabras, y que
# indique cuál de ellas es la más larga y por cuántas letras lo es.


# Pide al usuario ingresar dos palabras
palabra_1 = str(input("Palabra 1: "))
palabra_2 = str(input("Palabra 2: "))

# Obtener longitud de la cadena
lon_1 = len(palabra_1)
lon_2 = len(palabra_2)

# Imprime cual palabra es mas larga y por cuanto lo es
if lon_1 > lon_2 :
    diferencia = int(lon_1 - lon_2)
    print("La palabra", palabra_1, "tiene", diferencia, "letras mas que", palabra_2)
elif lon_2 > lon_1 :
    diferencia = int(lon_2 - lon_1)
    print("La palabra", palabra_2, "tiene", diferencia, " letras mas que", palabra_1)
else :
    print("Las dos palabras tienen el mismo largo")