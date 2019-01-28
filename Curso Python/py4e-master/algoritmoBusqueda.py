#este algoritmo sirve para buscar y obviar las lineas en blanco, tambien se cuentan las
#lineas en blanco al final
con = 0
fhand = open('mbox2.txt')
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting lines'
    if not line.startswith('From:'):
        con = con + 1
        print(con)
        continue
    # Process our 'interesting' line
    print(line)
print(con)
