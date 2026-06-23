class Aluno:
    
    
    def realizarProva(self, nome, ra):
        self.nome = nome
        self.ra = ra
        print(f"Hoje é dia de prova : {nome}")
        return
        
    def estudar(self, nome):
        self.nome= nome
        print(f"Esta estudando neste momento não é {nome}")    
        return
    
    