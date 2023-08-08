import math

class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def area(self):
        return self.comprimento * self.largura

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return 0.5 * self.base * self.altura

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * self.raio ** 2
    
class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"