#Open the file romeo.txt and read it line by line. For each line, split the line into a 
#list of words using the split() method. The program should build a list of words. 
#For each word on each line check to see if the word is already in the list and if 
#not append it to the list. When the program completes, sort and print the resulting 
#words in alphabetical order. 
words2 = []
fin = ""
fname = input("Enter file name: ")
fh = open(fname)
for words in fh:
	words2.append(words)
fin = str(words2)
print(sorted(list(set(fin.split()))))

print('ESTE PROGRAMA DA EL RESULTADO DESEADO, PERO NO SE USA EL METODO SPLIT() Y POR ESO ESTA MALO')