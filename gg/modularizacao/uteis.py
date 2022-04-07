
def fatorial(n):
    f = 1
    for i in range (1, n+1):
        f *= i
    return f

def dobro(n):
    return n * 2

def aumentar(n, p):
    return n * (p/100) + n

def diminuir(n, p):
    return (n * (p/100) - n)*-1

def metade (n):
    return n / 2

def moeda(n):
    n.replace('.', ',')

def resumo(n, a, r):
    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'O preço analisado é R${n}')
    print(f'A metade de {n} é {metade(n)}')
    print(f'O dobro de {n} é {dobro(n)}')
    print(f'Aumentando em {a}%, temos {aumentar(n, a)}')
    print(f'Diminuindo em {r}%, temos {diminuir(n, r)}')
    print('-'*30)