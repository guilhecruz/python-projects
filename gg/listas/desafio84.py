galera = list()
dados = list()
resp = 'S'
while True:
    if resp in "S":
        dados.append(str(input("Digite o nome da pessoa: ")))
        dados.append(int(input("Digite o peso da pessoa: ")))
        galera.append(dados[:])
        dados.clear()
        resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    else:
        print("Programa finalizado\n", "-"*30)
        break

print(f"Você cadastrou {len(galera[0])+1} pessoas")


for p in galera:
    if p[1] >= 100:
        print(f"As pessoas mais pesadas são {p[0]}")
    elif p[1] <= 70:
        print(f"As pessoas mais leves são {p[0]}")
