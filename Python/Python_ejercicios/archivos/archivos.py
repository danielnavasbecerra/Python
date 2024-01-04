file = open("Python/Python_ejercicios/archivos/archivo.txt")
print(file.read(),'\n')
file.close()

file = open("Python/Python_ejercicios/archivos/archivo.txt", "r")
print(file.read())
file.close()

file =  open("Python/Python_ejercicios/archivos/nuevoArchivo.txt", "w") 
file.write("Hola mundo")
file.close()