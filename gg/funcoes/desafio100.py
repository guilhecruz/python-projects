from random import randint
from time import sleep
def sorteia(lista):
    print("Os números sorteados foram: ", end='')
    for c in range (0,5):
        número = randint(0,10)
        print(f'{número}',flush=True, end =' ')
        sleep(0.5)
        lista.append(número)
    print("FIM")
    
def somaPar(lista):
    somaPares = 0
    for n in lista:
        if n%2 == 0:
            somaPares += n
    print(f'Os números fornecidos foram {lista}, e a soma dos pares foi de {somaPares}')

lista = []

sorteia(lista)
print(lista)
somaPar(lista)


#PQ AS VEZES SE COLOCA ALGUMA COISA DENTRO DA FUNÇÃO, OUTRAS NÃO? O QUE VAI DENTRO DA FUNÇÃO?