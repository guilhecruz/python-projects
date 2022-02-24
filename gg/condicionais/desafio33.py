a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

#Verificando o menor valor
menor = a

if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

#Verificando o maior valor
maior = a

if b>a and b>a:
    maior = b
if c>a and c>b:
    maior = c

print(f"O menor valor é {menor}")
print(f"O maior valor é {maior}")



''''
n1 = int(input("Qual o primeiro número? "))
n2 = int(input("Qual o segundo número? "))
n3 = int(input("Qual o terceiro número? "))


if n1 > n3 and n1 > n2:
    print(f"O maior número é {n1}")
    if n2 > n3:
        print(f"O menor número é {n3}")
    else:
        print(f"O menor número e {n2}")
elif n1> n3 and n1 < n2:
    print(f"O maior número é {n2}")
    print(f"O menor número é {n3}")
elif n3 > n2:
    print(f"O maior número é {n3}")
    if n2 > n1:
        print(f"O menor número é {n1}")
    else:
        print(f"O menor número e {n2}")
else:
    print(f"O maior número é {n2}")
    print(f"O menor número é {n1}")'''