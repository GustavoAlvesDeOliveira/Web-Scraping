class Carro:

    def __init__(self, cor):
        self.cor = cor
        self.motor = 0
        self.Consumo_de_gasolina = 0

    def pintarcarro(self, cor):
        self.cor = cor

    def motor(self, motor):
        self.motor = motor

    def Consumo_de_gasolina(self):
        self.Consumo_de_gasolina += 10

meu_carro = Carro("Azul")
print(meu_carro)

