fhand = open('mbox-short.txt')
print("THIS PROGRAM SELECT A # OF WORD FOR EACH LINE")
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[3])
	
	