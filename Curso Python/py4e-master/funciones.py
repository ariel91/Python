def computepay(h,r):
	calculo = ((40*r) + ((h-40)*r*1.5) )
	return calculo

hrs = 45
rate = 10.50

mifuncion= computepay(hrs,rate)
print(mifuncion)
