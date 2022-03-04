
'''
1 - perguntar ao user qual o valor que deseja sacar
2 - informar quantas cédulas de cada valor serão entregues
3 - cédulas de 50, 20, 10 e 1
'''
valor = cinq = vin = dez = uni = cedulas = 0
condição = "s"

while condição == "s":
    valor = int(input("Qual o valor que você deseja sacar? "))
    cinq = valor.index[0]
    print(cinq)

#print('''Serão entregues:
#{cinq} notas de 50
#{vin} notas de 20
#{dez} notas de 10
#{uni} notas de 1''')
