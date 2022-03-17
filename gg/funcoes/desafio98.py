from time import sleep

def contador(inicio, fim, passo):
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end =' ', flush = True)
            sleep(0.5)
            cont += passo
        print('fim')
        
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush = True)
            sleep(0.5)
            cont -= passo
        print('fim')
        print("-="*20) 

contador(1,10,1)
contador(10,0,2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
if p < 0:
    p *= -1
elif p == 0:
    p = 1
contador(i,f,p)