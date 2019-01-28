text = ''
con = 0
num2 = 0.0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    con = con + 1
    extract = line.find('0.')
    num1=float(line[extract::1])
    num2 = num2 + num1

print("Number of lines:" + str(con))
print("Sumatoria de numeros" + str(num2))
print("Promedio" + str(float(num2/con)))
print("Done")

#print(float(line[extract::1])) con esta linea puedo ver todos los numeros
