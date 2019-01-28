#DICCIONARIOS
#PODEMOS ASIGNAR VALORES, ACTUALIZAR, ELIMINAR Y BUSCAR.
#En caso busquemos un valor y no lo encontremos, la funcion GET nos permite devolver un valor de respuesta.

word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
print('---------------------------------------------------')
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)