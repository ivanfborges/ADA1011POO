class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __repr__(self):
        return f"Fracao({self.numerador}, {self.denominador})"

    def __add__(self, outra):
        return Fracao(self.numerador * outra.denominador + outra.numerador * self.denominador, self.denominador * outra.denominador)

    def __sub__(self, outra):
        return Fracao(self.numerador * outra.denominador - outra.numerador * self.denominador, self.denominador * outra.denominador)

    def __mul__(self, outra):
        return Fracao(self.numerador * outra.numerador, self.denominador * outra.denominador)

    def __truediv__(self, outra):
        return Fracao(self.numerador * outra.denominador, self.denominador * outra.numerador)


if __name__ == "__main__":
    f1 = Fracao(1, 2)
    f2 = Fracao(3, 4)

    print(f1 + f2)
    print(f1 - f2)
    print(f1 * f2)
    print(f1 / f2)