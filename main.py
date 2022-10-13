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
#
    essai = 0

    print("J'ai choisi un chiffre de 1 à 100")
    print("Essaye de le deviner!")

    boucle_essai = True
    while boucle_essai:


        choix_du_joueur = int(input("Choisissez un nombre de 1 à 100 "))


        essai = essai + 1

        if choix_du_joueur < nombre_aleatoire:
            print("Non, ton chiffre est trop petit")

        if choix_du_joueur > nombre_aleatoire:
            print("Non, ton chiffre est trop grand!")

        if choix_du_joueur == nombre_aleatoire:
            print("Bonne réponse! J avais effectivement choisi",nombre_aleatoire)
            rejouer = input("Voulez-vous rejouer?")
            if rejouer == "oui":
                boucle_essai = False

            if rejouer == "non":
                boucle_jeu = False
                boucle_essai = False