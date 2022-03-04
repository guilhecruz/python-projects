'''
1 - perguntar ao user qual o valor que deseja sacar
2 - informar quantas cédulas de cada valor serão entregues
3 - cédulas de 50, 20, 10 e 1
'''

valor = int(input("Digite o valor que você deseja sacar: R$ "))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f"O total de {totalced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
            totalced += 1
        elif ced == 20:
            ced = 10
            totalced += 1
        elif ced == 10:
            ced = 1
            totalced += 1
        totalced = 0
        if total == 0:
            break
print("-"*20,"\nVolte sempre! Tenha um Bom dia\n","-"*20)
