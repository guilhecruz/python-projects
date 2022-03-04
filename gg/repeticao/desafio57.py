#MEU
'''sexo = str(input("Digite o seu sexo (M/F): "))

while sexo in "Mm" or sexo in "Ff": 
    if sexo in "Mm":    
        print(f"Você digitou {sexo}. Você se considera um homem.")
    elif sexo in "Ff":
        print(f"Você digitou {sexo}. Você se considera uma mulher.")
    else:    
        print("ERRO!")
        print(input("Digite novamente: "))
    exit()'''

#Resolução
sexo = str(input("Digite o seu sexo (M/F): ")).strip().upper()[0]

while sexo not in "MmFf": 
   sexo = str(input("Dados inválidos. Digite novamente: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")











'''n = 1
par = impar = 0

while n != 0:
    n = int(input("Digite um valor: "))
    if n%2 == 0:
        par += 1
    else:
        impar += 1
print(f"Você digitou {par} número pares e {impar} números ímpares")'''