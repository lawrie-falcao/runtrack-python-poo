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
    def __init__(self, matiereEnseignee, age):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer")


eleve = Eleve(age=15)

eleve.bonjour()

eleve.allerEnCours()

eleve.modifierAge(15)

professeur = Professeur(matiereEnseignee="Mathématiques", age=40)

professeur.bonjour()

professeur.enseigner()
