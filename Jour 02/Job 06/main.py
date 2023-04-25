class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Année :", self.annee)
        print("Prix :", self.prix)


class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, portes=4):
        super().__init__(marque, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes :", self.portes)


# Instanciation d'un objet Voiture
ma_voiture = Voiture("Renault", 2022, 20000, 5)

# Appel de la méthode informationsVehicule de la classe Voiture pour afficher les informations de la voiture
ma_voiture.informationsVehicule()
