class Curso:
    
    def __init__(self, nome, email, telefone, id, desconto):
        
        self.nome= nome
        self.email= email
        self.telefone = telefone
        self.id = id
        self.desconto = desconto
    
    
    @property
    
    def getNome(self, _nome):
        self.nome= _nome
        return
    
    @property
    def setNome(self, _nome):
        self.nome= _nome
        
     
    
    