'''
1 - quantas vezes aparece o número 9
2 - em que posição está o número 3
3 - mostrar os números pares
'''

tupla = (int(input("digite um número: ")),
       int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")),
       int(input("Digite o último número: ")))

print(f"Você digitiou os valores {tupla} ")
print(f"O valor 9 apareceu {tupla.count(9)} vezes")

if 3 in tupla:
    print(f"O número 3 apareceu na {tupla.index(3)+1}ª posição")
else:
    print("O número 3 não foi digitado nesta sequência")

print("Os valores pares digitados foram: ", end='')
for n in tupla:
    if n%2 == 0:
        print(n, end =' ')
