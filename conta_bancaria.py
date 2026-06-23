class ContaBancaria:
    taxa_juros = 0.05
    
    def __init__(self,titular,saldo_inicial=0):
        self.titular = titular
        self.saldo_inicial=  saldo_inicial
        self.historico=[]
        pass
    def depositar(self, valor):
        if valor <= 0:
            return "Valor inválido para depósito."
        self.saldo += valor
        self.historico.append(f"Depósito: +R\${valor:.2f}")
        return f"Depósito de R\${valor:.2f} realizado. Saldo: R\${self.saldo:.2f}"
    
    def sacar(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente!"
        self.saldo -= valor
        self.historico.append(f"Saque: -R\${valor:.2f}")
        return f"Saque de R\${valor:.2f} realizado. Saldo: R\${self.saldo:.2f}"
    
    def extrato(self):
        print(f"--- Extrato de {self.titular} ---")
        for operacao in self.historico:
            print(f"  {operacao}")
        print(f"  Saldo atual: R\${self.saldo:.2f}")
        
    # Usando a classe
conta = ContaBancaria("Ana Silva", 1000)
print(conta.depositar(500))    # Saldo: R$1500.00
print(conta.sacar(200))        # Saldo: R$1300.00
conta.extrato()    