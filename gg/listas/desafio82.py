'''
1 - pedir vários números ►
2 - perguntar se quer continaur ►
3 - mostrar todos os números
4 - mostrar os pares
5 - mostrar os ímpares
'''

lista = list()
pares = list()
ímpares = list()
while True:
    n = lista.append(int(input("Digite um número: ")))
    resp = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if resp not in "S":
        break
print(f"Os valores digitados foram {lista}")

for c, n in enumerate(lista):
    if n%2 == 0:
        pares.append(n)
    else:
        ímpares.append(n)

print(f"Os valores pares são {pares}")
print(f"Os valores ímpares são {ímpares}")

