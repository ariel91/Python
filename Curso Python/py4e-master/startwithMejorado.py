fhand = open('mbox2.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
		
		
