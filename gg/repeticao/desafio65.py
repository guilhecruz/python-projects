valores = menor = maior = cont = soma = 0
decisao = "S"
while decisao in "S":
    valores = int(input("Digite um número: ")) 
    if valores > maior:
        maior = valores
    else:
        menor = valores
    decisao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    cont += 1
    soma = soma + valores

    media = soma/cont
print(f"Você digitou {cont} valores e a média deles foi {media}")
print(f"Você digitou {cont} valores. O maior valor foi {maior} e o menor foi {menor}")

