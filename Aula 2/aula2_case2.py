class Cliente:
    def __init__(self, nome, sobrenome, CPF):
        self.nome = nome
        self.sobrenome = sobrenome
        self.CPF = CPF

    def __str__(self):
        return f"Cliente {self.nome} {self.sobrenome} CPF {self.CPF}"


class Conta:
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

    def __str__(self):
        return f"Conta {self.numero} - Saldo: {self.saldo} - Cliente: {self.cliente}"


cliente1 = Cliente("João", "Silva", "123.456.789-00")
conta1 = Conta(123456, 1000, cliente1)

print(cliente1)
print(conta1)