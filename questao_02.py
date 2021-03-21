class Televisao:
     def __init__(self, canalInicial):
           self.ligada = False
           self.canal = canalInicial
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

tv1 = Televisao(9)

print(tv1.canal)