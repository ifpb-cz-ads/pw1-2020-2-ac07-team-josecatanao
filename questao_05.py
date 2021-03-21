class Televisao:
     def __init__(self, mini=2 , maxi = 14):
           self.ligada = False
           self.canal = 1
           self.canalmaxi = maxi
           self.canalmini = mini
           self.tamanho = 0
           self.marca = ''
     def muda_canal_para_baixo(self):
           self.canal -= 1
           self.canal = self.canalmaxi
     def muda_canal_para_cima(self):
           self.canal += 1
           self.canal = self.canalmini
     def adiciona_tamanho(self,valor):
          self.tamanho = valor
     def adiciona_marca(self,marca):
          self.marca = marca

tv1= Televisao(4,6)
print(tv1.canalmaxi)
print(tv1.canalmini)


tv2= Televisao(3,5)
print(tv2.canalmaxi)
print(tv2.canalmini)