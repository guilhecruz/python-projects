from datetime import date

id = int(input("Digite o seu ano de nascimento:"))
date = date.today().year
idade = date -id

if idade == 18:
    print("Já está no ano do seu alistamento")
elif idade < 18:
    idade = 18 - idade
    print(f"Ainda faltam {idade} anos para o seu alistamento")
elif idade > 18:
    idade = idade - 18
    print(f"Já se passaram {idade} anos do seu tempo de alistamento")