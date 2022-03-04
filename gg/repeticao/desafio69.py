'''
1 -  cadastrar idade e sexo dos usuários
2 - perguntar se o quer continuar
3 - contador com pessoas +18
4 - contador de pessoas do sexo masculino
5 - contador de mulheres com menos de 20 anos
'''
homens = mulheres20 = p18 = 0
condição = "s"

while condição != "n":
    idade = int(input("Qual a sua idade? "))
    sexo = str(input("Qual o seu sexo? [M/F]")).strip().lower()[0]
    if idade >=18:
        p18 += 1
    while sexo not in "mf":
        sexo = str(input("Dado inválido. Tente novamente. [M/F]")).strip().lower()[0]
    if sexo in "m":
        homens += 1
    if sexo in "f" and idade < 20:
        mulheres20 += 1
    print("-"*20)
    condição = str(input("Deseja continuar? [S/N]")).strip().lower()[0]
    print("-"*20)
print(f'''A quantidade de  homens foi de: {homens}; de mulheres com menos de 20 anos foi de: {mulheres20} 
e de pessoas com mais de 18 anos foi de:{p18}''')