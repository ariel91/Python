#busca todas las lineas que inician con FROM:
fhand = open('mbox2.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)
