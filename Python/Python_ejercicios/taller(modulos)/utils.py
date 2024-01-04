def ingresar_dato_numerico(enunciado):
    while True:
        dato = input(enunciado)
        if dato.isdigit():
            return int(dato)
        else:
            print("Error, el dato no es númerico")

def ingresar_dato_cadena(enunciado):
    while True:
        dato = input(enunciado)
        if dato.isalpha():
            return str(dato)
        else:
            print("Error, el dato no es una cadena")

def ingresar_dato_positivo(enunciado):
    while True:
        dato = input(enunciado)
        if dato.lstrip('-').isdigit():  # Verifica si el dato es un número (puede ser negativo)
            numero = int(dato)
            if numero > 0:
                print("El número es positivo")
                return numero
            else:
                print("Error: el número no es positivo. Ingrese un número positivo.")
        else:
            print("Error: el dato no es numérico.")