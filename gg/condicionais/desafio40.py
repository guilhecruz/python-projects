n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

m = (n1 + n2) /2

if m >=7:
    print("APROVADO!")
elif m <= 6.9 and m >= 5:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")