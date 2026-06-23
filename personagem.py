class Personagem:
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida
    
    def status(self):
        return f"🎮 {self.nome} | HP: {self.vida}"

class Guerreiro(Personagem):
    def __init__(self, nome, forca=10, **kwargs):
        super().__init__(nome, **kwargs)
        self.forca = forca
    
    def atacar(self, alvo):
        dano = self.forca * 2
        alvo.vida -= dano
        return f"⚔️ {self.nome} ataca {alvo.nome} causando {dano} de dano!"

class Mago(Personagem):
    def __init__(self, nome, mana=50, **kwargs):
        super().__init__(nome, **kwargs)
        self.mana = mana
    
    def lançar_magia(self, alvo, custo=10):
        if self.mana < custo:
            return "Mana insuficiente! 💫"
        self.mana -= custo
        dano = custo * 3
        alvo.vida -= dano
        return f"🔮 {self.nome} lança magia em {alvo.nome} causando {dano} de dano!"

# Herança Múltipla!
class Paladino(Guerreiro, Mago):
    def __init__(self, nome):
        super().__init__(nome, forca=8, mana=30, vida=120)
    
    def golpe_sagrado(self, alvo):
        if self.mana >= 5:
            self.mana -= 5
            dano = self.forca * 3
            alvo.vida -= dano
            return f"✨ Golpe Sagrado! {dano} de dano em {alvo.nome}!"
        return self.atacar(alvo)

# Batalha!
paladino = Paladino("Arthas")
inimigo = Personagem("Dragão", vida=200)

print(paladino.status())
print(paladino.atacar(inimigo))
print(paladino.lançar_magia(inimigo))
print(paladino.golpe_sagrado(inimigo))
print(inimigo.status())

# MRO - Method Resolution Order
print(Paladino.__mro__)