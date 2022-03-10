jogador = {}
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range (0, tot):
        partidas.append(int(input(f"    Quantos gols {jogador['nome']} fez na {c+1}ª partida")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar?")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! Por favor, resonda S ou N")
    if resp == "N":
        break
print('-'*40)
print('cod:', end = ' ')
for i in jogador.keys():
    print(f'{i:<15}', end ='')
print()

#USAR ENUMERATE PQ É LISTA
for k, v in enumerate(time):

    print(f'{k:>4}', end =' ')
    for d in v.values():
        print(f'{str(d):<15}', end ='')
    print()
print('-'*40)

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar)"))
    if busca == 999:
        break
    if busca >=len(time):
        print(f'Erro! Não exite jogador com código {busca} ')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca-1]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-'*40)
print(" >>> VOLTE SEMPRE <<<")