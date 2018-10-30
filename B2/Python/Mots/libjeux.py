import random
def getRandomWord():
	file = open('/home/shoxx/Documents/Cours/B1/Python/Mots/dico.txt', 'r')
	postion = random.randint(1,3000)
	x=0
	mot_a_trouver=""
	for line in file:
		if(x==postion):
			mot_a_trouver=line
			break
		x+=1
	mot_a_trouver=mot_a_trouver[:-1]
	return mot_a_trouver