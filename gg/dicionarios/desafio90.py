'''
1 - perguntar o nome do aluno
2 - perguntar a média do aluno
3 - mostrar a situação do aluno (aprovado ou reprovado)
'''


'''
aluno = {}
alunos = []
resp = 's'
while True:
    aluno['nome'] = str(input("Nome: "))
    aluno['média'] = float(input("Média: "))
    alunos.append(aluno.copy())
    if aluno['média']>=7:
        print(f"Situação de {aluno['nome']}, com média de {aluno['média']}: Aprovado")
    if 5 <= aluno['média'] <7:
        print(f"Situação de {aluno['nome']}, com média de {aluno['média']}: Recuperação")
    else:
        print(f"Situação de {aluno['nome']}, com média de {aluno['média']}: Reprovado")
    resp = str(input("Quer continuar?"))
    if resp in "nN":
        print("Encerrando o programa...")
        break

print(alunos)
'''
 #I
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
 #K     #V
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recueração'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
