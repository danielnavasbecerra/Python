import json

estudiantes = []
"nro de identificación": ["", ""]
"nombre": ["", ""]
"Apellidos": ["", ""]
"dirección": ["", ""]
"acudiente": ["", ""]
"teléfonos de contacto(Nro celular y nro fijo)": ["", ""]
"estado": ["", ""]

# Pasamos el diccionario a objeto tipo json
things = json.dumps(estudiantes)

# usamos open para abrir el archivo o para generarlo si no existe y abrirlo
file =  open("things.json", "w") 

# Escribimos sobre todo el archivo
file.write(things)

# Cerramos el archivo
file.close()