class Forme:
    def aire(self):
        return 0

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
        
    def aire(self):
        return 3.14 * self.radius ** 2

rectangle = Forme()

cercle = Cercle(5)

print(rectangle.aire()) # affiche 0
print(cercle.aire()) # affiche 78.5
