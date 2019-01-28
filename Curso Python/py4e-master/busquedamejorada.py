con = 0
fhand = open('mbox2.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        con = con + 1
        print(con)
        print(line)
print(con)
