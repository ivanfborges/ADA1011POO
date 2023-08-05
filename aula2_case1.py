class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
        # Função para simplificar a fração
        divisor_comum = self.mdc(self.numerador, self.denominador)
        self.numerador //= divisor_comum
        self.denominador //= divisor_comum

    def mdc(self, a, b):
        # Função para calcular o maior divisor comum (MDC)
        while b:
            a, b = b, a % b
        return a

    def __add__(self, fracao2):
        # Operação de adição de frações
        numerador = self.numerador * fracao2.denominador + self.denominador * fracao2.numerador
        denominador = self.denominador * fracao2.denominador
        fracao_resultante = Fracao(numerador, denominador)
        fracao_resultante.simplificar()
        return fracao_resultante

    def __sub__(self, fracao2):
        # Operação de subtração de frações
        numerador = self.numerador * fracao2.denominador - self.denominador * fracao2.numerador
        denominador = self.denominador * fracao2.denominador
        fracao_resultante = Fracao(numerador, denominador)
        fracao_resultante.simplificar()
        return fracao_resultante

    def __mult__(self, fracao2):
        # Operação de multiplicação de frações
        numerador = self.numerador * fracao2.numerador
        denominador = self.denominador * fracao2.denominador
        fracao_resultante = Fracao(numerador, denominador)
        fracao_resultante.simplificar()
        return fracao_resultante

    def __div__(self, fracao2):
        # Operação de divisão de frações
        numerador = self.numerador * fracao2.denominador
        denominador = self.denominador * fracao2.numerador
        fracao_resultante = Fracao(numerador, denominador)
        fracao_resultante.simplificar()
        return fracao_resultante
    
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


# Testando a classe Fracao
frac1 = Fracao(3, 4)
frac2 = Fracao(1, 2)

print("Fração 1:", frac1)
print("Fração 2:", frac2)

# Adição
result_add = frac1 + frac2
print("Resultado da adição:", result_add)

# Subtração
result_sub = frac1 - frac2
print("Resultado da subtração:", result_sub)

# Multiplicação
result_mult = frac1 * frac2
print("Resultado da multiplicação:", result_mult)

# Divisão
result_div = frac1 / frac2
print("Resultado da divisão:", result_div)