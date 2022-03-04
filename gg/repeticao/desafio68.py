from random import randint
soma = cont = cpu = usernumber = 0

'''
1 - escolha impar ou par
2 - escolha um número
3 - somar os números da cpu com user
4 - chegar o resto da soma dividio por 2
5 - se o resto da soma for 0 e o user for par, user ganha
6- se não, user perde, programa encerra.
'''
vitória = 0

while vitória != 1 :
    cpu = randint(0,10)
    print(cpu)
    usernumber = int(input("Qual número você escolhe? "))
    userchoice = str(input("Você escolhe ímpar ou par? ")).strip().upper()[0]
    while userchoice not in "IP":
        userchoice = str(input("Opção errada. Digite novamente. Ímpar ou par")).strip().upper()[0]
    soma = cpu + usernumber
    if soma%2 == 0 and userchoice == "P":
        print("Você ganhou! Vamos de novo.")
    else:
        vitória += 1
        print("Você perdeu! Programa encerrado...")

