import random
numero1 = random.randrange(1,10)
numero2 = random.randrange(1,10)
numero3 = random.randrange(1,10)
numero4 = random.randrange(1,10)
numero5 = random.randrange(1,10)
tuple = numero1, numero2, numero3, numero4, numero5

menor = maior = 0

for c in tuple:
    if c > maior:
        maior = c
    else:
        menor = c


print(f"Os números gerados foram{tuple}")
print(f'O maior valor sorteado foi {max(tuple)}')
print(f'O menor valor sorteado foi {min(tuple)}')
'''print(f"O maior número foi {maior}")
print(f"O menor número foi {menor}")'''