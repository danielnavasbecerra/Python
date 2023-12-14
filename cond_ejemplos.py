haceFrio = True
llueve = False
abrigado = None
sombrillaAbierta = None

if(haceFrio):
	abrigado = True
else:
	abrigado = False


if(llueve):
	sombrillaAbierta = True
else:
	sombrillaAbierta = False

print("abrigado:", abrigado)     # imprime True   // por que haceFrio es verdadero
print("sombrillaAbierta:", sombrillaAbierta) # imprime False por que llueve es falso