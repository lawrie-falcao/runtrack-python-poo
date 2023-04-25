import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        couleurs = ["Coeur", "Carreau", "Pique", "Trèfle"]
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger(self):
        random.shuffle(self.paquet)

    def distribuer(self):
        return self.paquet.pop()

class Main:
    def __init__(self):
        self.cartes = []
        self.total = 0

    def ajouter_carte(self, carte):
        self.cartes.append(carte)
        if carte.valeur == "As":
            if self.total + 11 > 21:
                self.total += 1
            else:
                self.total += 11
        elif carte.valeur in ["Valet", "Dame", "Roi"]:
            self.total += 10
        else:
            self.total += int(carte.valeur)

    def afficher(self):
        for carte in self.cartes:
            print(carte.valeur, "de", carte.couleur)
        print("Total :", self.total)

class JeuBlackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.jeu.melanger()
        self.main_joueur = Main()
        self.main_croupier = Main()

    def jouer(self):
        # Distribution des cartes
        for i in range(2):
            self.main_joueur.ajouter_carte(self.jeu.distribuer())
            self.main_croupier.ajouter_carte(self.jeu.distribuer())
        print("Main du joueur :")
        self.main_joueur.afficher()
        print("Main du croupier :")
        print(self.main_croupier.cartes[0].valeur, "de", self.main_croupier.cartes[0].couleur)

        # Tour du joueur
        while True:
            choix = input("Voulez-vous prendre une carte (p) ou passer (q) ? ")
            if choix == "p":
                self.main_joueur.ajouter_carte(self.jeu.distribuer())
                self.main_joueur.afficher()
                if self.main_joueur.total > 21:
                    print("Vous avez perdu !")
                    return
            elif choix == "q":
                break

        # Tour du croupier
        while self.main_croupier.total < 17:
            self.main_croupier.ajouter_carte(self.jeu.distribuer())
        print("Main du croupier :")
        self.main_croupier.afficher()

        # Résultat
        if self.main_joueur.total > 21:
            print("Vous avez perdu !")
        elif self.main_croupier.total > 21:
            print("Vous avez gagné !")
        elif self.main_joueur.total > self.main_croupier.total:
            print("Vous avez gagné !")
        elif self.main_joueur.total < self.main_croupier.total:
            print("Vous avez perdu !")
        else:
            print("")
