color = input('Qué color?: ')
colores = ('rojo', 'azul', 'verde', 'amarillo')

if color in colores[0]:
	print('El color rojo está admitido')
elif color in colores[1]:
	print('El color azul está admitido')
elif color in colores[2]:
	print('El color verde está admitido')
elif color in colores[3]:
	print('El color amarillo está admitido')
else:
	print('Ese color no se acepta')
