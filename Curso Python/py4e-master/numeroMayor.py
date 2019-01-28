num = int(input('¿Cuántos números vas a introducir?: '))
listaNumeros = []
for a in range(num):
    numero = int(input("Dime un número: "))
    listaNumeros.append(numero)

print('El número mayor es el {}'.format(max(listaNumeros)))
print('El número menor es el {}'.format(min(listaNumeros)))
