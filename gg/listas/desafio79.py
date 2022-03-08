'''
1 - pedir um valor e adicionar em uma lista ►
2 - perguntar se quer continuar ►
3 - recusar valor duplicado
4 - encerrar quando não quiser mais continuar ► 
5 - mostrar os valores em ordem crescente ►
'''

listanum = list()
condição = "S"

while True:
    if condição == 'S':
        n = int(input("Digite um valor: "))
        if n not in listanum:
            listanum.append(n)    
            print("Valor adicionado com sucesso")
        else:
            print("Valor duplicado. Não vou adicionar.")
        condição = str(input("Você deseja continuar? [S/N]")).strip().upper()[0]
    else:
        break

print(f"Os valores inseridos na lista foram {sorted(listanum)}")