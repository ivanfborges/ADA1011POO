class Cliente:
    def __init__(self, nome, sobrenome, CPF):
        self.nome = nome
        self.sobrenome = sobrenome
        self.CPF = self.validar_cpf(CPF)
        self.contas = []

    def adicionar_conta(self, conta):
        if conta not in self.contas:
            self.contas.append(conta)
        else:
            print("Cliente já possui esta conta.")

    def validar_cpf(self, CPF):
        cpf_digits = [int(digit) for digit in CPF if digit.isnumeric()]
        cpf_to_validate = cpf_digits[:-2]
        validador_n1 = self.calcular_digito_verificador(cpf_to_validate)

        if str(validador_n1) != str(cpf_digits[-2]):
            raise ValueError("CPF inválido!")

        cpf_to_validate.append(validador_n1)
        validador_n2 = self.calcular_digito_verificador(cpf_to_validate)

        if str(validador_n1) + str(validador_n2) == "".join(map(str, cpf_digits[-2:])):
            return CPF
        else:
            raise ValueError("CPF inválido!")

    def calcular_digito_verificador(self, cpf_part):
        fixa = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        validador = list(zip(cpf_part, fixa))
        validador = [a * b for (a, b) in validador]
        soma = sum(validador)
        resto = soma % 11
        if resto < 2:
            return 0
        return 11 - resto

    def __str__(self):
        return f"Cliente: {self.nome} {self.sobrenome}\nCPF: {self.CPF}\n"

class Conta:
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente
        cliente.adicionar_conta(self)

    def __str__(self):
        return f"Conta {self.numero} - Saldo: {self.saldo}\nTitular da Conta\n{self.cliente}"
   
# Testando
 
cliente2 = Cliente("José", "Santos", "061.543.102-00")
conta2 = Conta(234567, 2000, cliente2)

print(cliente2)
print(conta2)

cliente1 = Cliente("João", "Silva", "337.609.182-04")
conta1 = Conta(123456, 1000, cliente1)

print(cliente1)
print(conta1)