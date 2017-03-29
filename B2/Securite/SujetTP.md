#Hebergement de solutions sécurisés

L'objectif cette année est de proposer une solution d'hébergement. 
Evidemment sécurisé.

Sous objectifs : 
	Avoir une interface de "commande":
		Sur cette interface un client pourra choisir le type de service dont il a besoin.
	Avoir une interface "client":
		Sur cette interface le client retrouve la liste de ses services.

	Types de services : 
		* Web :
			L'hosting web classique à la sauce OVH : Un serveur web, une base de données, un accès FTP.
		VPS Low Level: 
			Une machine linux standard avec accès SSH
		VPS HighLevel:
			Une machine linux standard avec accès SSH  ( accès root ) 

	Le déployement de ses solutions doit se faire le plus rapidement possible.
	(cherchez donc à automatiser)
	N'oubliez pas l'expérience utilisateur qui est très importante ! 

	A votre disposition : 
		Une machine Debian. 

* Votre objectif prioritaire. 

Piste de recherche : 
	IPTables, Droits unix, chroot, container, reverse proxy .. 

	
Comme toujours, tout ce que vous développez doit etre sécurisé. 
Ainsi vous pouvez attaquer vos concurents, sur le même principe que l'an dernier, chaque vulnérabilité trouvée vous rapporte des points :
	
	Vuln découverte : 100pts
	Accès utilisateur applicatif : 200pts
	Accès root : 500pts

Les règles de cette partie attaque / défense sont les suivantes :
	
	Pas d'attaques physiques ( reglez vos comptes aux flechettes )
	Pas de destruction du travail d'autruit (vous avez un accès root, vous avez finit rien a faire de plus)
	Reportez tout ce que vous trouvez par mail a l'équipe adverse + moi en copie. 


Evaluation :

	L'évaluation se fera en 2 étapes. 

	Tout d'abord vos services d'hebergement seront évalués sur leur fonctionnement. 
		Je vous soummeterais une demande d'hebergement.
		Le contenu que je ferais hebergé sera volontairement remplis de faille afin de tester le comportement de votre application.

	Une presentation technico-comericale:
		Comerciale parce qu'on vous demandera souvent de faire cet exercice à l'école donc profitons en. 
		Technique parce qu'après tout c'est surtout ce qui nous interesse ! 
		
