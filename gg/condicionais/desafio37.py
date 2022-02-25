num = int(input("Diite um número inteiro: "))
print('''Escolha uma das bases para conversão:
[1] BIN
[2] OCTA
[3] HEXA''')
opção = int(input("Sua opção: "))

if opção == 1:
    print(f"{num} convertido para BINÁRIO é igual a{bin(num)[2:]}")
elif opção == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif opção == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("Opção inválida. Tente novamente")
