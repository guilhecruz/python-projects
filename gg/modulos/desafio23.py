num = int(input("Digite um número: "))

un = num // 1 % 10
dez = num // 10 %10
cen = num // 100 %10
mil = num // 1000 %10

print(f"unidade: {un}\n dezena: {dez}\n centena: {cen}\n milhar: {mil}")