numero = int(input("Digite um número inteiro: "))
fatorial = numero
cont = numero
#==========================MEU==========================
while cont > 0:
    if (cont-1) == 0:
        print(f"O fatorial de {fatorial} é {numero}")
        exit()
    else:    
        n = numero * (cont-1)
        cont -= 1
#==========================RESOLUÇÃO==========================
while cont > 0:
    print("{}".format(fatorial, end = ''))
    print(' x ' if c> 1 else '=', end = '')
    f *= c
    c -= 1
print("O fatorial de {} é {}".format(numero, fatorial))

#==========================USANDO BIBLIOTECA==========================
from math import factorial
n = int(input("Digitre um número para calcular seu Fatorial"))
f = factorial(n)
print("O fatorial de {} é {}".format(n,f))