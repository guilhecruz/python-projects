sal = float(input("Qual o seu salário atual? "))

if sal > 1.250:
    sal = sal + (sal*0.10)
    print(f"Seu salário passsará ser {sal}")
else:
    sal = sal + (sal*0.15)
    print(f"Seu salário passará a ser {sal}")