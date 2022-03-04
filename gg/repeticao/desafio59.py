a = float(input("Insira o primeiro valor: "))
b = float(input("Insira o segundo valor: "))

op = 0
while op != 5:
    print("-=-"*10)
    op = input("Você deseja:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa\n")
    print("-=-"*10)
    if op == "1":
        soma = a + b
        print(f"A soma do valores é igual a {soma}")
    elif op == "2":
        mult = a * b
        print(f"O resultado da operação é {mult}")
    elif op == "3":
        if a > b:
            print(f"O maior valor é {a}")
        else:
            print(f"O maior valor é {b}")
    elif op == "4":
        a = float(input("Insira o novo primeiro valor: "))
        b = float(input("Insira o novo segundo valor: "))
    elif op == "5":
        print("Finalizando...")
    else:
        print("ERRO. Tente novamente")
