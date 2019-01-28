#num = int(input('¿Cuántos números vas a introducir?: '))
cont=0
menor=999999
mayor = 0
listaNumeros = []
num = ''
while num != 'done':
    num = input ('Ingrese numero:')
    if num == "done":
        print('Proceso terminado')
    else:
        numeros=int(num)
        listaNumeros.append(numeros)
        if mayor<numeros:
            mayor=numeros
        if menor>numeros:
            menor=numeros

print('El número mayor es el ' + str(mayor))
print('El número menor es el ' + str(menor))
