
def teste(b):
    b += 4
    c = 2
    print(f'O valor de a é {a}')
    print(f'O valor de b é {b}')
    print(f'O valor de c é {c}')

a = 5
teste(a)


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f"Os resultados são: {f1}, {f2} e {f3}")

def par (n=0):
    if n%2 == 0:
        return True
    else:
        return False

num = int(input("Digite um número: "))
if par(num):
    print('É par')
else:
    print("É ímpar")