import time
debut=time.time()
file = open('dico.txt', 'r')
for lines in file:
	print lines
fin=time.time()

print str(fin-debut)
