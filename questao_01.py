class Televisao:
     def __init__(self):
           self.ligada = False
           self.canal = 2
           self.tamanho = 0
           self.marca = ''
     def muda_canal_para_baixo(self):
           self.canal -= 1
     def muda_canal_para_cima(self):
           self.canal += 1
     def adiciona_tamanho(self,valor):
          self.tamanho = valor
     def adiciona_marca(self,marca):
          self.marca = marca


tv1 = Televisao()
tv2 = Televisao()

tv1.adiciona_tamanho(10)
tv1.adiciona_marca('Sansung')

tv2.adiciona_tamanho(15)
tv2.adiciona_marca('Philips')

print(tv1.tamanho)
print(tv1.marca)

print(tv2.tamanho)
print(tv2.marca)




