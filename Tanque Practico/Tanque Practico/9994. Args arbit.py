print("4")
print("3")
print("1")
print("2")
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')
colores("azul","purple")

def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de sumar estos cinco números es:', resultado)

suma(5, 7, 45, 8657, 3, 4)