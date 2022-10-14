"""Créé par Philippe Coutu
Groupe 406
29 Septembre 2022
TDescription: Jeu de devinette dans lequel le joueur doit deviner un chiffre aléatoire sur 100, le code lui dit si son
chiffre est plus haut ou plus bas qye le chiffre à deviner
"""




import random

#Je crée une boucle dans laquelle le jeu sera joué, si le joueur finit le jeu et dit non à la question finale, il quitte la boucle et le jeu est terminé")
boucle_jeu = True

while boucle_jeu:
    nombre_aleatoire = random.randint(0, 100)

# Variable qui sert à calculer le nombre d'essais pour l'afficher au joueur
    essai = 0

#Variable qui permet au joueur de choisir de nombre minimum dans le choix de nombres aléatoires
    nombre_minimum = int(input("Choisissez le nombre minimum du jeu"))

# Variable qui permet au joueur de choisir de nombre minimum dans le choix de nombres aléatoires
    nombre_maximum = int(input("Choisissez le nombre maximum du jeu"))
#Variable qui choisis un nombre aléatoire entre le nombre minum et le nombre maximum choisis par le joueur
    nombre_choisi = random.randint(nombre_minimum, nombre_maximum)


    print("Essayez de deviner le nombre aléatoire entre les bornes de votre choix!")

# Boucle dans laquelle la partie sera jouée, si le joueur termine une partie et decide de recommencer, la boucle recommence
    boucle_essai = True

    while boucle_essai:

        essai = essai + 1

        print("Essai numero" ,essai )

#Variable qui sert à faire deviner le nombre aléatoire, le joueur recoit ce message et doit donner une réponse de 1 à 100
        choix_du_joueur = int(input("Choisissez un nombre"))

#Ce qui arrive si le chiffre est trop petit
        if choix_du_joueur < nombre_choisi:
            print("Non, ton chiffre est trop petit")

#Ce qui arrive si le chiffre est trop grand
        if choix_du_joueur > nombre_choisi:
            print("Non, ton chiffre est trop grand!")

#Ce qui arrive si le joueur choisis le bon nombre
        if choix_du_joueur == nombre_choisi:
            print("Bonne réponse! Le chiffre était",nombre_choisi)

# Variable qui sert à demander au joueur si il veut quitter le code ou rejouer
            rejouer = input("Voulez-vous rejouer?")
            if rejouer == "oui":
                boucle_essai = False

            if rejouer == "non":
                boucle_jeu = False
                boucle_essai = False