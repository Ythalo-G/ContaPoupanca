# Classe para implementar uma classe poupança
# Os atributos serão: numero conta , nome, saldo
# Teremos os metodos alterar nome. deposito e saque
# Lembre que o saldo poderá começar com zero por padrão

class Conta():
    def __init__(self, numeroConta, nome, saldo):
        self.numeroConta = numeroConta
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, nome):
        self.nome = nome
    def depositar (self, valor):
        self.saldo += valor
    def saque (self, valor):
        self.saldo -= valor



cliente = Conta("001","Marcos", 0)
print(vars(cliente))

cliente.alterarNome("Ricardo")
print(vars(cliente))

cliente.depositar(1800)
print(vars(cliente))

cliente.saque(500)
print(vars(cliente))

resposta = input("Deseja consultar Extrato ? S- sim / N não")
if ( resposta == "S"):
    Conta.extratoBancario()

