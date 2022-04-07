try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b   
     
except (ValueError, TypeError):
    print('\033[0;31mTivemos um erro com os tipos de dados inseridos\033[m')
except ZeroDivisionError:
    print('\033[0;31mNão é possível dividir um número por zero\033[m')
except KeyboardInterrupt:
    print('\033[0;31mUsuário preferiu não informar os dados\033[m')
except Exception as erro:
    print(f'Encontramos um problema: {erro.__cause__}')    
else:
    print(f'O resultado é {r:.1f}')
#Acontece independente se deu certo ou errado
finally:
    print('Volte sempre! Muito obrigado!')