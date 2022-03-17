def fatorial(num=1, mostra = False):
    n = 1
    for c in range(num, 0, -1):
        if mostra:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' =', end = ' ')
        n *= c
    return n

print(fatorial(5, mostra = True))

'''
resp = 'N'

n = int(input('Digite um número: '))
n1 = fatorial(n)

resp = str(input('Você deseja mostrar a operação? [S/N]')).upper()
print(f"O fatorial de {n} é {n1}")
'''