'''
1 - cirar um dicionário que leia nome, ano de nascimento e carteira de trabalho
2 - cadastrar a pessoa com idade
3 - se a pessoa tiver ctps, pedir ano da contratação e salário
4 - mostrar os dados inseridos e com quantos anos a pessoa vai se aposentar
'''
from datetime import datetime
pessoa = {}

pessoa['nome'] =  str(input("Nome: "))
nascimento = int(input("Ano de nascimento: "))
pessoa['idade'] = datetime.now().year - nascimento
pessoa['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))

if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input("Ano de contratação: "))
    pessoa['Salário'] = float(input("Salário: "))
    pessoa['aposentadoria'] = (pessoa['idade']) + ((pessoa['contratação'] + 35) - datetime.now().year)
    
print('-='*30, '\nDados inseridos:')
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')

