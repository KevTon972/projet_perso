#!/usr/bin/env python3
# trouver le nombre mystere
import random

nombre_mystere = random.randint(1, 50)
nombre_essai = 5
nombre_rater = 1

print("*** Le jeu du nombre mystere *** ")

while nombre_essai != 0:

    print(f"il te reste {nombre_essai} essai")

    user_choice = input("devine le nombre : ")

    if not user_choice.isdigit():
        print(" veuillez entrer un nombre valide ! ")
        continue

    elif int(user_choice) != nombre_mystere:
        if int(user_choice) > nombre_mystere:
            print(f"le nombre mystere est plus petit que {user_choice}. ")

        else:
            print(f"le nombre mystere est plus grand que {user_choice}. ")
    else:
        print(f"Bravo le nombre mystere etait bien {nombre_mystere}")
        print(f"tu as trouve le nombre en {nombre_rater} essai. ")
        print("fin du jeu. ")
        exit()

    nombre_essai -= 1
    nombre_rater += 1

if nombre_essai == 0:
    print(f"Dommage le nombre mystere etait {nombre_mystere}. ")

print("fin du jeu. ")    