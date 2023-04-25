class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True
        
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre
        
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur
        
    def get_nb_pages(self):
        return self.__nb_pages
    
    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Erreur : le nombre de pages doit être un entier positif.")
    
    def est_disponible(self):
        return self.__disponible
    
    def emprunter(self):
        if self.est_disponible():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible pour le moment.")
    
    def rendre(self):
        if not self.est_disponible():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")

    def afficher_livre(self):
        print("Titre :", self.__titre)
        print("Auteur :", self.__auteur)
        print("Nombre de pages :", self.__nb_pages)
        print("Disponible :", self.__disponible)

livre1 = Livre("Le Rouge et le Noir", "Stendhal", 500)

livre1.afficher_livre()

if livre1.est_disponible():
    print("Le livre est disponible.")
else:
    print("Le livre n'est pas disponible.")

livre1.emprunter()

if livre1.est_disponible():
    print("Le livre est disponible.")
else:
    print("Le livre n'est pas disponible.")