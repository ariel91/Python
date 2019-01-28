con = 0
fhand = open('mbox2.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    con = con + 1
    print(con)
    print(line)
