produto = num = 1

while num > 0:
    print("-"*30)
    num = int(input("Qual número você deseja ver a tabuada? "))
    print("-"*30)
    if num >= 0:
        cont = 0
        while cont < 10:
            cont += 1   
            produto = num * cont
            print(f"{num} * {cont} = {produto}")        
    else:
        print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
        break
