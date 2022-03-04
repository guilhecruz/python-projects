num = soma = cont = 0

while num != 999:
    if num == 999:
        print(f"A soma dos {cont} valores digitados é igual a: {soma}")
        print("Saindo do programa. Até a próxima...")
    soma = soma + num
    cont += 1
    num = int(input("Digite um número (999 para parar): "))
print(f"A soma dos {cont} valores digitados é igual a: {soma}")
print("Saindo do programa. Até a próxima...")
