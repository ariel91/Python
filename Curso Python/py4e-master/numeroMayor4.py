listaNumeros = []
num = ''
while True:
	try:
		num = input('Ingrese numero:')
		if num == "done":
			break			
		else:
			numeros= int(num)
	num = input('Ingrese numero:')
	if num == "done":
		break
	else:
		try:
			numeros = int(num)
			listaNumeros.append(numeros)
			mayor = max(listaNumeros)
			menor = min(listaNumeros)
	except:
		print('Invalid input')
		continue
print('Maxium is ' + str(mayor))
print('Minium is ' + str(menor))
		except:
			print('Invalid input')
			continue
print('Maximum is {}'.format(max(listaNumeros)))
print('Minimum is {}'.format(min(listaNumeros)))
