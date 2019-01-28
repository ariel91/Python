menor=999999
mayor = 0
listaNumeros = []
num = ''
while True:
	num = input ('Ingrese numero:')
	if num == "done":
		break
	else:
		try:
			numeros = int(num)
			listaNumeros.append(numeros)
		except:
			print('Invalid input')
			continue
print('Maximum is {}'.format(max(listaNumeros)))
print('Minimum is {}'.format(min(listaNumeros)))
