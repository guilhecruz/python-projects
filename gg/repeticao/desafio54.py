from datetime import date
b = 0
d = 0
for c in range (1,8):
    a = int(input("Digite o ano do seu nascimento: "))
    a = date.today().year - a

    if a >= 21:
        b += 1
    else: 
        d += 1
print(f"{b} pessoas já atigiriam a maior idade e {d} pessoas ainda não atingiram a maior idade")