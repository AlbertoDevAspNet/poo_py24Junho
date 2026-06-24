class CursoProtegido:
    def __init__(self,nome,email,telefone,id,senha):
        self_nome= nome
        self_email =email
        self_telefone = telefone
        self_id= id
        self_senha= senha
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor:
            self._nome = valor
        else:
            raise ValueError("Nome deve ser uma string não vazia.") 
        
    @property
    def email(self):
        return self._nome

    @email.setter
    def email(self, valor):
        if isinstance(valor, str) and valor:
            self.email = valor
        else:
            raise ValueError("Nome deve ser uma string não vazia.") 

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        if isinstance(valor, str) and valor:
            self._telefone = valor
        else:
            raise ValueError("Nome deve ser uma string não vazia.") 
        
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        if isinstance(valor, int) and valor:
            self._id = valor
        else:
            raise ValueError("Nome deve ser uma string não vazia.") 
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if isinstance(valor, str) and valor:
            self._senha = valor
        else:
            raise ValueError("Nome deve ser uma string não vazia.") 
    

    