from random import randint
from time import sleep
from operator import itemgetter 
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}

ranking = list()

print('Valores sorteados:')

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.75)
print(jogo)
#Colocando dicionário na ordem crescente
ranking = sorted(jogo.items(), key = (itemgetter(1)), reverse = True)
print('-='*30,'\n == Ranking dos Jogadores ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)