'''
1 - ler o nome do produto ►
2 - ler o preço do produto ►
3 - perguntar se o usuário quer continuar►
4 - mostrar o total gasto na compra ►
5 - quantos produtos custaram mais de R$1000 ►
6 - qual o nome do produto mais barato
'''

preço = total = quantidade = maiscaro = maisbarato = maismil = 0
condição = "s"
nomemaisbarato = "a"

while condição == "s":
    nomeproduto = str(input("Qual o nome do produto? ")).strip().lower()
    preço = float(input("Qual o preço do produto: "))
    #COMPARANDO PREÇOS
    if preço > maiscaro:
        maiscaro = preço
    else:
        maisbarato = preço
        #SALVANDO NOME DO PRODUTO MAIS BARATO
        nomemaisbarato = nomeproduto
    if preço > 1000:
        maismil += 1
    #TOTAL DA COMPRA
    total = total + preço
    #PERGUNTANDO SE O USUÁRIO AINDA QUER CONTINUAR
    condição = str(input("deseja continuar? [S/N]")).strip().lower()[0]

print(f'''Total gasto na compra: {total}
Produtos que custaram mais de R$1000: {maismil}
Nome do produto mais barato: {nomemaisbarato}
Valor do produto mais barato: {maisbarato}
Valor do produto mais caro{maiscaro}''')
        