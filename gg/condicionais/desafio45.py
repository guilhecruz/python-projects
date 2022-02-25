import random
from  time import sleep
import emoji

print("VAMOS JOGAR JOKENPÔ!")

pe = emoji.emojize(":fist:" , use_aliases = True)
pa = emoji.emojize(":raised_hand:" , use_aliases = True)
te = emoji.emojize(":v:" , use_aliases = True)
op = [pe, pa, te]
cpu = random.choice(op)
us = int(input(f"escolha: \n1 - {pe}\n2 - {pa} \n3 - {te} \n"))

print("-=-"*20,("\nEscolhendo\n"),"-=-"*20)
sleep(1.5)

if us == 1:
    us = pe
    us == pe
    print(pe)
elif us == 2:
    us == pa
    print(pa)
elif us == 3:
    us == te
    print(te)

print (cpu)  

if us == cpu:
    print("EMPATE! Vamos de novo")
elif us == pe and cpu == te:
    print("Parabéns, você me venceu!")
elif us == pe and cpu == pa:
    print("GANHEI!")
elif us == 2 and cpu == pe:
    print("Parabéns, você me venceu!")
elif us == 2 and cpu == te:
    print("GANHEI!")
elif us == 3 and cpu == pa:
    print("Parabéns, você me venceu!")
elif us == 3 and cpu == pe:
    print("GANHEI!")
else:
    print("ERRO")