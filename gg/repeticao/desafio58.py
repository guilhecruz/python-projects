from random import randint
from re import T
computador = randint(0,10)

print("Sou seu computador.. Acabei de pensar em um número entre 0 e 10\n Será que você consegue adivinhar qual foi? ")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite"))
    palpite+=1
    if jogador == computador:
        acertou = T
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez")
        else:
            print("Menos... Tente mais uma vez")
print(f"Acertou com {palpite} tentativas, mizeravi")







#MEU
'''from random import randint
from time import sleep
n =  randint(0,10)
print("-=-"*20)
print("Vou pensar em um número entre 0 a 10. Tente adivinhar...")
print("-=-"*20)

nu = int(input("Qual foi o número que o computador pensou? "))
print("PROCESSANDO...")
sleep(1.5)

cont = 1
while nu != n:
    cont += 1
    print("Errado!")
    print(int(input("Tente novamente: ")))
    
if nu == n:
    print(f"Parabéns, você acertou na {cont}ª tentativa")'''
