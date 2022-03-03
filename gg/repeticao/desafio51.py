i = int(input("Digite o primeiro termo da PA: "))
p = int(input("Digite a razão da PA: "))
d = i + (10-1) * p
for c in range (i, d+p, p):
    print(c,end="-> ")
print("FIM")