''''
8) Crie classes para representar estados e cidades. Cada estado tem um nome, sigla e cidades. Cada cidade tem nome e população. Escreva um programa de testes que crie três estados com algumas cidades em cada um. Exiba a população de cada estado como a soma da população de suas cidades.
'''

class Estados:
  def __init__(self, nome, sigla, cidades,popu):
    self.nome = nome
    self.sigla = sigla
    self.cidades = cidades
    self.populacao = popu

paraiba = Estados('paraiba','PB',['sousa','cajazeiras','aparecida'],[10,30,40])
ceara = Estados('Ceará','CE',['Erere','Ico','Belem'],[50,80,60])
saoPaulo = Estados('São paulo','SP',['Bauru','suzano','maúa'],[90,80,100])

print("Estado:",paraiba.nome ,"População: ",sum(paraiba.populacao))
print("Estado:",ceara.nome ,"População: ",sum(ceara.populacao))
print("Estado:",saoPaulo.nome ,"População: ",sum(saoPaulo.populacao))



   