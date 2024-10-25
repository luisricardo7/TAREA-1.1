# Clase Rectangulo

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

# Creando una instancia de Rectangulo con base 5 y altura 3
rectangulo = Rectangulo(5, 3)

area_rectangulo = rectangulo.area()
perimetro_rectangulo = rectangulo.perimetro()
print(area_rectangulo, perimetro_rectangulo)
