# coding: utf8
# Ouvrir un fichier
# Manipuler Open / Read / Write
import libjeux
import draw

motATrouver=libjeux.getRandomWord()

print motATrouver

nbVies=8
trouve=False
print "========="
print "| Pendu |"
print "========="

actualWord = ["-"]*(len(motATrouver))
actualWord[0]=motATrouver[0]
print "".join(actualWord)

essais = []

while nbVies>0 and trouve==False:
	foundOne=False
	lettre = raw_input('Entrez une lettre : ')
	for i in range(0,len(motATrouver)):
		if(motATrouver[i]==lettre[0]):
			foundOne=True
			actualWord[i]=lettre[0]
	if(foundOne==False):
		nbVies-=1
	trouve=True
	for i in actualWord:
		if(i=="-"):
			trouve=False
	essais.append(lettre[0])
	print "".join(actualWord)
	print "%s vies restante"%(nbVies)

	print draw.status(nbVies)


	print "Vous avez essaye les lettres : %s"%("".join(essais))
if(trouve):
	print "Trouvé !"
else:
	print "Mort :)"