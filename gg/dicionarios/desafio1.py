aluno = dict()
média = 0
aluno['nome'] = str(input("Nome do aluno: "))
aluno['média'] = float(input("Média do aluno: "))

if 5 <= aluno['média'] < 7:
    print(f'Situação de {aluno["nome"]}: Recuperação')
elif aluno['média'] >= 7:
    print(f'Situação de {aluno["nome"]}: Aprovado')
else:
    print(f'Sitação de {aluno["nome"]}: Reprovado')


