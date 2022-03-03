somaidade = 0
mediadidade = 0
maioridade = 0
nomevelho =""
totmulher = 0
for p in range(1,5):
    print(f"{p}ª Pessoa")
    nome = str(input("Qual o seu nome? ")).strip()
    idade = int(input("Qual a sua idade? "))
    sexo = str(input("Qual o seu sexo? (M/F)")).strip()
    somaidade += idade

    if p == 1 and sexo in "Mm":
        maioridade = idade
        nomevelho = nome
    if sexo in "Mm" and idade>maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in "Ff" and idade <20:
        totmulher += 1
    

m = somaidade/4
print(f"A média de idade do grupo  é de {m} anos.")
print(f"O homem com maior idade foi {nomevelho} com {maioridade} ")
print(f"Ao todo são, {totmulher} com menos de 20 anos")