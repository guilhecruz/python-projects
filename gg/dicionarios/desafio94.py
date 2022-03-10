pessoa = dict()
galera = list()
soma = média = 0
#CADASTRANDO AS PESSOAS
while True:
    pessoa.clear
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo: ")).upper()[0]
        if pessoa['sexo'] in "MF":
            break
        print("Erro! Digite M ou F")
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar? ")).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if resp == 'N':
        break
print('-='*30)
print(galera)

#PESSOAS CADASTRADAS
print(f'Ao todo, temos {len(galera)} pessoas cadastradas')
#MÉDIA DE IDADE
média = soma/len(galera)
print(f'A média de idade é de {média:5.2f} anos.')
#PRINTANDO OS NOMES DAS MULHERES CADASTRADAS
print('As mulheres cadastradas foram  ', end ='')
for p in galera:
    if pessoa['sexo'] == 'F':
        print(f'{p["nome"]}', end =',')
print()
#PESSOAS COM IDADE ACIMA DA MÉDIA
print('Lista das pessoas que estão acima da média ', end ='')
for p in galera:
    if p['idade'] >= média:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v};', end ='')
        print()
print("ENCERRANDO...")
