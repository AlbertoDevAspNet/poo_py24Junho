class Pessoa:
    # Atributo de classe (compartilhado)
    especie = "Homo sapiens"
    
    def __init__(self, nome, idade, profissao):
        # Atributos de instância (únicos por objeto)
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def apresentar(self):
        return f"Olá! Sou {self.nome}, tenho {self.idade} anos e sou {self.profissao}."
    
    def fazer_aniversario(self):
        self.idade += 1
        return f"Parabéns {self.nome}! Agora você tem {self.idade} anos! 🎂"
# Criando objetos (instâncias)
maria = Pessoa("Maria", 28, "engenheira")
joao = Pessoa("João", 35, "professor")
print(maria.apresentar())
# Olá! Sou Maria, tenho 28 anos e sou engenheira.
print(joao.fazer_aniversario())
# Parabéns João! Agora você tem 36 anos! 🎂
# Atributo de classe é o mesmo para todos
print(maria.especie)  # Homo sapiens
print(joao.especie)   # Homo sapiens

