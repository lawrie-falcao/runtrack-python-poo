class Personne:
    def __init__(self, age=14):
        self.age = age
        
    def afficherAge(self):
        print("J'ai", self.age, "ans")
        
    def bonjour(self):
        print("Hello")
        
    def modifierAge(self, newAge):
        self.age = newAge


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
        
    def affichageAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer")

personne = Personne()
eleve = Eleve()

print("Age de l'élève par défaut:", eleve.age)
