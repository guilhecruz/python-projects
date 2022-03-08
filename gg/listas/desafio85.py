num = [[],[]]

for n in range (1,8):
    valor = int(input(f"Digite o {n}º número: "))
    if valor%2 == 0:
        num[0].append(valor)
        #num.clear()
    else:
        num[1].append(valor)
        #num.clear()
            
print(f"Os números digitados foram {num}")
num[0].sort()
print(f"Os número pares foram {num[0]}")
num[1].sort()
print(f"Os números ímpares foram {num[1]}")