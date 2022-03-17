from random import randint
from time import sleep
from operator import itemgetter

resultados = list()
jogadores = []
ranking = []


for c in range (0,4):
    resultados = {f'jogador {c+1}' : randint(1,6)}
    print (resultados)
    sleep(0.75)
    jogadores.append(resultados.copy())
print()
print(jogadores)
print()
                                           #ORDEM DE VALOR
ranking = sorted(resultados.items(), key = (itemgetter(1)), reverse = True)
print()

for i, v in enumerate(ranking):
    print(f'{i} -> {v}')

    #DUVIDA DUVIDA DUVIDA DUVIDA DUVIDA DUVIDA
    #COMO FAZER ELE MOSTRAR O RANKING DE TODOS OS JOGADORES USANDO FOR