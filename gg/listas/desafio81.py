'''
1 - Pedir um valor ►
2 - Perguntar se quer continuar ►
3 - Mostrar quantos valores foram digitados ►
4 - Mostrar os valores de forma decrescente (reverse=True)
5 - mostrar se o valor "5" faz parte da lista
'''
valores = list()
resp = "S"

while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if resp not in "S":
        break

print(f"Você digitou {len(valores)} valore(s)")
valores.sort(reverse=True)
print(f"Os elementos de forma decrescente são: {valores}")

if 5 in valores:
    print(f"O valor 5 está na {valores.index(5)+1}ª posição")
else:
    print("Não foi digitado o valor 5 nesta sequência")