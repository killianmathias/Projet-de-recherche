Au cours de notre cursus L2 CMI Informatique, nous avons eu l'occasion de travailler sur un projet de recherche. Le sujet de ce projet de recherche est la génération procédurale de décors.
Notre objectif est donc de reproduire une version simplifiée de Terraria en générant les blocs de manière à créer des montagnes, des plaines, etc. On souhaiterait également s'orienter vers la génération de biomes, de grottes et éventuellement de minerais.
Pour arriver à ce but, nous devons donc rechercher des algorithmes procéduraux qui peuvent répondre à nos besoins. Dans un premier temps, pour générer les blocs de manière procédurale, nous souhaitons nous orienter vers le bruit de Perlin, puis pour les autres fonctionnalités nous n'avons pas encore recherché d'algorithmes répondant à ces besoins. De plus, nous devons prendre en compte l'optimisation de cette génération, notamment le bruit de Perlin afin de pas générer toute la map en 1 seule fois mais plutôt sous forme de chunk (zone de génération).
![Exemple de Terraria](https://raw.githubusercontent.com/killianmathias/Projet-de-recherche/main/assets/toundra.png)

Afin de parvenir à notre but de réalisation du Terraria simplifié, nous avons choisi Python et sa bibliothèque Pygame car cette dernière simplifié tout ce qui concerne l'application visuelle, ce qui nous permettra donc de nous focaliser sur l'implémentation des algorithmes de génération procédurale.

Pour en savoir un peu plus, je vous invite à consulter notre rapport de recherche.

![Exemple de notre implémentation](https://raw.githubusercontent.com/killianmathias/Projet-de-recherche/main/assets/background_1.png)
