
try:
    fhand = open('mbox-short.txt')	
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    if line.startswith('From:'):
        word = line.split()[1]
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

#print(counts)
max_sent_count = max(counts.values())
for sender, count in counts.items():
    if count == max_sent_count:
        print(sender, count)
