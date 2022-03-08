'''dados = list()
dados.append("Pedro")
dados.append(25)
print(dados[0])
print(dados[1])

pessoas = list()
pessoas.append(dados[:])
print(pessoas)'''
'''
#Lista assumindo dados de outra lista
teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = "maria"
teste[1] = 22
galera.append(teste[:])
print(galera)

#Printando apenas os nomes
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
'''

galera = list()
dado = list()
totmai = totmen = 0
for c in range (0,3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade")
        totmen += 1
print(f"Temos {totmai} maiores de idade e {totmen} menores de idade")