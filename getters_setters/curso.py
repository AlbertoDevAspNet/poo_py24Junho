class Curso:
    
    def __init__(self, nome, email, telefone, id, desconto):
        
        self._nome= nome
        self._email= email
        self._telefone = telefone
        self._id = id
        self._desconto = desconto
    
    
    @property
    
    def getNome(self, _nome):
        self.nome= _nome
        return
    
    @property
    def setNome(self, _nome):
        self.nome= _nome
        
     
    
    