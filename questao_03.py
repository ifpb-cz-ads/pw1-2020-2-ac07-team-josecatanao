class Televisao:
     def __init__(self, mini, maxi):
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


tv= Televisao(2,10)
tv.muda_canal_para_baixo()
print(tv.canal)

tv.muda_canal_para_cima()
print(tv.canal)




