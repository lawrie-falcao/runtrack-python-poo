class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
        
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
        
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
        
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
        
    def volume(self):
        return self.surface() * self.__hauteur
    

r = Rectangle(5, 3)
print("Longueur :", r.get_longueur())
print("Largeur :", r.get_largeur())
print("Perimetre :", r.perimetre())
print("Surface :", r.surface())

p = Parallelepipede(5, 3, 2)
print("Longueur :", p.get_longueur())
print("Largeur :", p.get_largeur())
print("Hauteur :", p.get_hauteur())
print("Perimetre :", p.perimetre())
print("Surface :", p.surface())
print("Volume :", p.volume())
