import hashlib

class Usuario:
    def __init__(self, username, senha):
        self.username = username
        self.__senha_hash = self.__hash_senha(senha)
        self.__tentativas_falhas = 0
        self.__bloqueado = False
    
    def __hash_senha(self, senha):
        """Método privado - converte senha em hash"""
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def autenticar(self, senha):
        if self.__bloqueado:
            return "Conta bloqueada! Contate o administrador."
        
        if self.__hash_senha(senha) == self.__senha_hash:
            self.__tentativas_falhas = 0
            return f"Bem-vindo, {self.username}! ✅"
        else:
            self.__tentativas_falhas += 1
            if self.__tentativas_falhas >= 3:
                self.__bloqueado = True
                return "Conta bloqueada após 3 tentativas! 🔒"
            restantes = 3 - self.__tentativas_falhas
            return f"Senha incorreta. {restantes} tentativa(s) restante(s). ❌"
    
    def alterar_senha(self, senha_atual, nova_senha):
        if self.__hash_senha(senha_atual) != self.__senha_hash:
            return "Senha atual incorreta!"
        if len(nova_senha) < 6:
            return "Nova senha deve ter pelo menos 6 caracteres!"
        self.__senha_hash = self.__hash_senha(nova_senha)
        return "Senha alterada com sucesso! 🔑"

user = Usuario("maria_dev", "python123")
print(user.autenticar("python123"))   # Bem-vindo!
print(user.autenticar("errada"))      # Senha incorreta. 2 tentativa(s)
print(user.alterar_senha("python123", "nova_senha_forte"))