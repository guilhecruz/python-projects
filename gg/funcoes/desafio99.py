from time import sleep
def maior(*parametros):
    cont = maior = 0
    print("Analisando os valores passado...")
    for valor in parametros:
        print(f"{valor}", end= ' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram {cont} valores ao todo')
    print(f'O maior valor foi {maior}')

#Programa Principal

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(0)