
carro_marca= "Toyota"
carro_modelo="Corolla"
carro_velocidade=0

def acelerar(velocidade_atual, incremento):
    return velocidade_atual + incremento
carro_velocidade = acelerar(carro_velocidade, 20)
print(f"Velocidade: {carro_velocidade} km/h")
# ✅ Abordagem Orientada a Objetos
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0
    
    def acelerar(self, incremento):
        self.velocidade += incremento
meu_carro = Carro("Toyota", "Corolla")
meu_carro.acelerar(20)
print(f"Velocidade: {meu_carro.velocidade} km/h")