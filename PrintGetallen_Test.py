print("Print getallen.")
getal = 123456789
counter = 0

while getal > 0: 
	print(getal)
	getal = int(getal/10)
	counter = counter + 1
	print("Aantel cijfers: ", counter)
