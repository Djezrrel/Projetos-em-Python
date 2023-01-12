class Car:
    def __init__(self, make, modelo, ano):
        self.make = make
        self.modelo = modelo
        self.ano = ano
        self.Velocidade = 0

    def Aceleração(self):
        self.Velocidade += 5

    def parada(self):
        if self.Velocidade >= 5:
            self.Velocidade -= 5

    def retornaVelocidade(self):
        return self.Velocidade

class CarroEletrico(Car):
    def __init__(self, make, modelo, ano):
        super().__init__(make, modelo, ano)
        self.nivelBateria = 100

    def usarBateria(self):
        if self.nivelBateria >= 10:
            self.nivelBateria -= 10
            self.Aceleração()

    def carregaBateria(self):
        self.nivelBateria += 10

    def get_nivelBateria(self):
        return self.nivelBateria

meuCarro = CarroEletrico("Uno", "Turbo com escada", 2000)
print(meuCarro.make, meuCarro.modelo, meuCarro.ano)
meuCarro.usarBateria()
print("Velocidade atual:", meuCarro.retornaVelocidade())
print("Nível da bateria:", meuCarro.get_nivelBateria())