contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')
condição = 'S'

while condição == 'S' :
    num = int(input("Digite um número: "))
    if 0 <= num <= 20:
        break
    print("Tente novamente.", end ='')
print("Você digitou o número {}".format(contagem[num]))   

condição = str(input(("Você deseja continuar? [S/N] "))).strip().upper()[0]