class Fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        return self.numerator * other.denominator != other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    
# Testando

frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

print(f"Fração 1: {frac1}")
print(f"Fração 2: {frac2}")
print(f"Fração 1 + Fração 2: {frac1 + frac2}")
print(f"Fração 1 - Fração 2: {frac1 - frac2}")
print(f"Fração 1 * Fração 2: {frac1 * frac2}")
print(f"Fração 1 / Fração 2: {frac1 / frac2}")
print(f"Fração 1 > Fração 2: {frac1 > frac2}")
print(f"Fração 1 > Fração 2: {frac1 < frac2}")
print(f"Fração 1 <= Fração 2: {frac1 >= frac2}")
print(f"Fração 1 <= Fração 2: {frac1 <= frac2}")
print(f"Fração 1 <= Fração 2: {frac1 == frac2}")
print(f"Fração 1 <= Fração 2: {frac1 != frac2}")