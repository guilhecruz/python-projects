from random import randint
from time import sleep
n =  randint(0,5)
print("-=-"*20)
print("Vou pensar em um número entre 0 a 5. Tente adivinhar...")
print("-=-"*20)

nu = int(input("Qual foi o número que o computador pensou? "))
print("PROCESSANDO...")
sleep(1.5)
if nu == n:
    print("Parabéns, você acertou!")
else:
    print(f"Ganhei! Eu pensei no número {n}")