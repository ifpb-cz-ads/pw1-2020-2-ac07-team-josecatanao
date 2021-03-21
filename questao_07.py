class Conta:
     def __init__(self, clientes, numero, saldo = 0):
         self.saldo = 0
         self.clientes = clientes
         self.numero = numero
         self.operacoes = []
         self.deposito(saldo)
     def resumo(self):
         print("CC",self.numero,"", self.clientes,"saldo :", self.saldo)
     def saque(self, valor):
         if self.saldo >= valor:
               self.saldo -= valor
               self.operacoes.append(["SAQUE", valor])
         else:
           print('saldo insuficiente')

     def deposito(self, valor):
         self.saldo += valor
         self.operacoes.append(["DEPÓSITO", valor])
     def extrato(self):
         print("Extrato CC N° %s\n" % self.numero)
         for o in self.operacoes:
               print("%10s %10.2f" % (o[0],o[1]))
         print("\n       Saldo: %10.2f\n" % self.saldo)

cli = Conta('jose',12,10)
cli.resumo()