class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def informationsVehicule(self):
        print(f"Marque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}")

    def demarrer(self):
        print("Attention, je roule")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee):
        super().__init__(marque, modele, annee)
        self.roue = 2
    
    def demarrer(self):
        print(f"Je démarre ma moto {self.modele} de {self.marque}")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee):
        super().__init__(marque, modele, annee)
        self.roue = 4
    
    def demarrer(self):
        print(f"Je démarre ma voiture {self.modele} de {self.marque}")

# Instancier un objet Voiture et un objet Moto et appeler leur méthode demarrer
voiture1 = Voiture("Peugeot", "308", 2022)
voiture1.demarrer()

moto1 = Moto("Yamaha", "R1", 2021)
moto1.demarrer()
