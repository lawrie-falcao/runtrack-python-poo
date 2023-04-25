class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def informationsVehicule(self):
        print(f"Marque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee):
        super().__init__(marque, modele, annee)
        self.roue = 2
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roue}")

# Instancier un objet Moto et appel de la méthode informationsVehicule
moto1 = Moto("Yamaha", "R1", 2021)
moto1.informationsVehicule()
