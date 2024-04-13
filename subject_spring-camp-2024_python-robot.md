---
module:			B-INN-000
title:			Spring Camp 2024
subtitle:		Python robot programming - Introduction

noFormalities:  true

author:			Mani Gillier
version:		1.0

#define linebreak \\vspace*{#1cm}
#define lb \#linebreak(1)
#define slb \#linebreak(0)
#define comment [comment]: <>(#1)

---

#imageCenter(firia-labs-logo.png, 500px)

# Le site internet

#largeText

/!\\\\ SITE EN ANGLAIS UNIQUEMENT

[sim.firialabs.com](https://sim.firialabs.com/ "Home page")

#lb

#imageCenter(firia-home-page, 400px)

#lb

La page d'accueil du site devrait ressembler à ça.
Vous pouvez:

  * **Creer un compte**
ou
  * **Continuer en tant qu'invite.**

# Detail de la fenetre

#imageCenter(mission-1.png, 500px)

#lb

#twoColumns(0.5,
    **Sur la gauche :**
    L'interface d'édition du code
    , **Sur la droite :**
    Les missions et la vue du robot
    )

# Votre objectif : reussir toutes les missions : 

## Premiere mission

#### Apprendre à utiliser l'interface. 

#smallText

#warn(Si vous avez besoin d'aide avec l'anglais, demandez à des personnes autours de vous, et si personne ne sait, aux *cobras*.)

#warn(Chaque mission est composée d'objectifs, qu'il faut réussir dans l'ordre pour valider la mission)

## Deuxieme mission

### Introduction au robot CodeBot
#lb
**C'est quoi un périphérique ?**
#slb
Le robot doit intéragir avec l'extérieur. Pour se faire, il possède des périphériques :
Un périphérique c'est un object électronique qui va :

  * Capter de l'information (capteur de distance par exemple)
  * Actionner quelque chose (moteur pour avancer par exemple)
  * Afficher quelque chose (LED ou Buzzer par exemple)

Le robot sur lequel on va travailler possèdes des périphériques que vous allez décrouvrir dans cette mission et certaines prochaines missions.
#lb
Vous allez devoir localiser différent périphériques avant de commencer à les programmer

## Troisieme mission
#lb
**Enfin de la programmation !**
Supprimez toutes les lignes de 4 à la fin.
(Gardez le `from botcore import *`)
#slb

### Petite introduction

#lb
Une fonction, c'est quoi ?
#slb
Une fonction c'est un action qui sera effectuée. Exemple : avancer.
Elle peut prendre des paramètres. Exemple : avancer(10 mètres).
#slb
En python on appelle une fonction comme ceci : `nom(argument_1, argument_2, ...)`
#slb
On vous donne dans le premier objectif l'exemple suivant :
`leds.user_num(0, True)`
La function user_num prends deux paramètres : l'identifiant de la LED à allumer, et son status (True ou False | Allumé ou éteint).
#slb
Exemple : si je veux allumer la LED N°2 (On commence à compter de 0 donc la troisème), je rajoute la ligne
`leds.user_num(2, True)`
#slb
Détail de la ligne : 
`leds` représente la liste des leds.
`user_num` représente l'action effectuée SUR cette liste de leds (allumer ou éteindre un élement en particulier)
`(2, True)` représente les arguments de l'action : led N°2, allumer)
#lb
Le binaire est un format de stockage de données : 
#slb
Plutôt que de stocker indépendamment l'état de chacune des leds, on va les stocker ensemble.
Exemple pour stocker l'état `Allume | Eteint | Allume | Eteint` des 4 premières leds,
on va les stocker avec des 0 ou de 1.
1 = Allumé
0 = Eteint.
Ca donne : 1010
(on nottera en python `0b1010`)
`0b` (zéro, b) étant le préfixe python pour indiquer un formatage binaire.

### Objectif 4

#lb
Pour allumer les leds du dessus du robot, on utilisait la fonction `user` ou `user_num`.
Pour allumer les autres leds, il existe d'autres fonctions variant selon l'emplacement des leds.
Elles marchent de la même manière que `user_num` et `user` respectivement.
Il y a :

  * `ls_num` et `ls` pour les leds sur le capteur de ligne (il y en a 5)
  * `prox_num` et `prox` pour les leds sur le capteur de proximité (il y en a 2)
  * `usb` (mettez juste l'état ici en argument, comme il n'y a qu'une seule LED, pas besoin de présicer laquelle allumer) pour la led sur la prise USB (une seule LED)
  * `pwr` (Marche comme la précédente) pour la led sur la prise de courant (une seule LED)

## Troisieme mission

#lb

Maintenant, essayez de comprendre par vous-même toutes les instructions données sur le site ! 
Vous retrouverez de nouvelles fonctions, que vous ne connaissez pas, alors étudiez le code donné par le `CodeTrek`.
Essayez de comprendre chaque argument donné dans les fonctions, et si besoin, demandez à vos camarades.

#hint(L'entraide avant tout !)

## Sandbox

#lb

Si vous avez fini la troisème mission, félicitation !
Vous avez fini cet exercice du spring camp.
#slb
Cependant, si vous voulez continuer, passez en mode SANDBOX (bouton en bas à droite)
Faites ce que vous voulez !
Testez des trucs :)
Le but : s'amuser, expérimenter, et apprendre
#lb
Quelques exemples rien que pour vous :

  * Faire un 8 avec le robot
  * Faire un triangle
  * Toucher les 4 balles de tennis de la troisieme mission, en moins de 1 minute puis moins de 30s
  * Aller en ligne droite, faire demi-tour, et revenir sur ses pas
  * Aller voir la documentation, et essayer de faire marcher les capteurs !
    * Une fois en sandbox, en bas de l'écran du robot, changer la map en `Line-follow 101`
  * Avec les capteurs qui marchent, faites en sorte de suivre les lignes et de finir le parcours !
