def leiaInt(msg):
    """
    Tratamento de erros para variáveis do tipo int
    :param msg: Mensagem a ser exibida para o usuário
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não informar o número.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    """
    Tratamento de erros para variáveis do tipo float
    :param msg: Mensagem a ser exibida para o usuário
    """
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não informar o número.\033[m')
            return 0
        else:
            return n

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O número inteiro foi {n1} e o número real foi {n2}')



'''
try:
    r1 = int(input('digite um número inteiro:'))

except (ValueError, TypeError):
    print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')
else:
    try:
        r2 = float(input('digite um número real:'))
    except (ValueError, TypeError):
        print('\033[0;31mERRO: Digite um número real válido.\033[m')
    else:
        print(f'O número inteiro foi {r1} e o número real foi {r2}')
'''