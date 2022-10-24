#!/usr/bin/env python3
#jeu de role
from random import randint

point_de_vie_perso = 50
point_de_vie_ennemie = 50
nombre_potion = 3

while point_de_vie_perso and point_de_vie_ennemie != 0:
    choix_utilisisateur = input("souhaitez-vous attaquer (1) ou souhaitez-vous une potion (2)? ")
    
    if not choix_utilisisateur.isdigit():
        continue
    
    elif int(choix_utilisisateur) >= 3:
        continue

    choix_utilisisateur = int(choix_utilisisateur)
    degat_perso = randint(5, 10)
    degat_ennemie = randint(5, 15)
    regain_de_vie = randint(15, 50)

    if choix_utilisisateur == 1:
        point_de_vie_ennemie -= degat_perso
        point_de_vie_perso -= degat_ennemie

        if point_de_vie_ennemie <= 0:
            print(f"vous avez infligé {degat_perso} points de degats a l'adversaire. ")
            print("Vous avez gagné !!! ")
            print("Fin de la partie! ")
            exit()
        else:
            print(f"vous avez infligé {degat_perso} points de degats a l'adversaire. ")

        if point_de_vie_perso <= 0:
            print(f"L'ennemie vous a infligé {degat_ennemie} points de degats. ")
            print("Vous avez perdu ...")
            print("Fin de la partie! ")
            exit()
        else:
            print(f"L'ennemie vous a infligé {degat_ennemie} points de degats. ")
            print(f"il vous reste {point_de_vie_perso} point de vie. ")
            print(f"il reste {point_de_vie_ennemie} point de vie a l'ennemie")

    elif choix_utilisisateur == 2:
        if nombre_potion == 0:
            print("Vous n'avez plus de potions. ")
            continue

        point_de_vie_perso += regain_de_vie
        point_de_vie_perso -= degat_ennemie
        nombre_potion -= 1

        print(f"Vous récuperez {regain_de_vie} point de vie ({nombre_potion} potions restante) ")
        print(f"L'ennemie vous a infligé {degat_ennemie} points de degats. ")
        print(f"il vous reste {point_de_vie_perso} point de vie. ")
        print(f"il reste {point_de_vie_ennemie} point de vie a l'ennemie")
        print("*"*45)

        point_de_vie_perso = point_de_vie_perso - degat_ennemie

        print("Vous passez votre tour... ")
        print(f"L'ennemie vous a infligé {degat_ennemie} points de degats. ")
        print(f"il vous reste {point_de_vie_perso} point de vie. ")
        print(f"il reste {point_de_vie_ennemie} point de vie a l'ennemie")
        
    print("*"*45)
