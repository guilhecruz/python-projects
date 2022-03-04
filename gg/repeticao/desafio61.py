print("-=-"*10,"\nGerador de PA\n", "-=-"*10)
primeiro = int(input("Digite o primeiro valor da PA: "))
razão = int(input("digite a razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} -> ", end ='')
        termo += razão
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos mais você quer mostrar? "))
print("Progressão finalizada com {} termos".format(total))