class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

mon_animal = Animal()
print(mon_animal.age)
mon_animal.vieillir()
print(mon_animal.age)
mon_animal.nommer("Luna")
print(mon_animal.prenom)