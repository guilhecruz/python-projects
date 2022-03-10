'''
1 - perguntar o nome do jogador
2 - quantas partidas o jogador jogou
3 - quantos gols ele fez em cada partida
4 - printar em dicionário
5 - printar cada key
6 - printar quantos gols o jogador fez em cada partida e quantos fez no total
'''

jogador = {}
partidas = list()

jogador['nome'] = str(input("Nome do jogador: "))

tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

for c in range(0,tot):
    partidas.append(int(input(f'   Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    

print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

jogador['totalgols'] = sum(partidas)
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["totalgols"]} gols')


'''
jogador = {}

nome = str(input("Nome do jogador: "))
jogador['nome'] =  nome


jogos = int(input(f'Quantas partidas o {nome} jogou? '))
jogador['jogos'] =  jogos
gols = 0 
if jogos > 0:
    for c in range(0, jogos):
        gols = int(input(f"Quantas gols {nome} fez? na {c}ª partida "))
        if gols > 0:
            gols += 1
jogador ['gols'] = gols
for v in jogador.values(jogador['gols']):
    print(f'O {nome} jogou {jogador['jogos']} partidas.')
    for c in range(jogador['jogos']):
        print(f'Na partida {c}, fez {jogador['gols[c]']}')
'''