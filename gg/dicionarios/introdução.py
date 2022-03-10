'''dados = {}
dados = {'nome':'Pedro', 'idade':'25'}
print(dados('nome')) #Pedro
print(dados('idade')) #25

#adicionando elemento
dados['sexo'] = 'M'
del dados['idade']'''
'''
filme = {'titulo':'Star Wars',
         'ano': '1977',
         'direto': 'George Lucas'
         }
print(filme.values()) #Star Wars, 1977, George Lucas #
print(filme.keys()) #título, ano, diretor
print(filme.items()) #Os 2

for key, value in filme.items():
    print(f'O {key} é {value}')
#CHAVES (CADA LISTA DENTRO DE UM DICIONÁRIO)
#VALUE (CADA VALOR DENTRO DE UMA LISTA PERTENCENTE AO DICIONÁRIO)
#ITEMS (CONJUNTO CHAVE E VALOR)

locadora = {{'título':'Star Wars', 'ano':'1977','diretor':'George Lucas'},{'título':'Avengers','ano':'2012','diretor':'Joss Whedon'},{'título':'Matrix','ano':'1999','diretor':'Wachowski'}}
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': "São Paulo", 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)'''

estado = {} #dicionário
brasil = [] #lista
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input("Sigla do Estado: "))
    #fazendo append da cópia de estado
    brasil.append(estado.copy())
for estado in brasil:
    for v in estado.values():
        print(v, end=' ')
    print()