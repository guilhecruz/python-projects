ficha = list()

while True:
    nome = str(input("Qual o nome do alunho? "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    média = (nota1 + nota2)/2
    ficha.append([nome,[nota1, nota2], média])

    resp = str(input("Quer continuar? ")).strip().upper()
    if resp in "N":
        break
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*35)
    opc = int(input("Mostrar a nota de qual aluno? "))
    if opc == 999:
        print('-'*10, "  Finalizando... ", '-'*10)
        break
    if opc <= len(ficha)-1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")
