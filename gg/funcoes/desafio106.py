from time import sleep

c = ('\033[m',        # 0 - sem cores
     '\033[0;30;41m', # 1 - Vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[0;30m'     # 6 - branco
     );

def ajuda(func):
    título(f'Acessando o manual do comando "{func}"', 4)
    print(c[6],end ='')
    help(func)
    print(c[0], end ='')
    sleep(2)

def título(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end = '')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end = ' ')
    sleep(1)

func = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    func = str(input("Funcão ou Biblioteca > "))
    if func.upper() == 'FIM':
        break
    else:
        ajuda(func)
título('Até logo', 1)
