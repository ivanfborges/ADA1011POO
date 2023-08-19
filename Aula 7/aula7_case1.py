class Veiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def __str__(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas

    def get_portas(self):
        return self.__portas

    def __str__(self):
        return f"Carro - {super().__str__()}, Portas: {self.__portas}"


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.__cilindradas = cilindradas

    def get_cilindradas(self):
        return self.__cilindradas

    def __str__(self):
        return f"Moto - {super().__str__()}, Cilindradas: {self.__cilindradas}"
    
# Main
carro = Carro("Renault", "Clio", 4)
moto = Moto("Honda", "Bros", 160)

veiculos = [carro, moto]

for veiculo in veiculos:
    print(veiculo)