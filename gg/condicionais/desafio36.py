print("Bem vindo ao EmprestCasa!")
casa = float(input("Informe o valor do imóvel: "))
sal = float(input("Informe o seu salário: "))
anos = int(input("Em quantos anos será financiada: "))
anos = anos*12
sal30 = sal + (sal*0.30)

if casa/anos < sal30:
    parcela = casa/anos
    print(f"O valor de cada parcela será {parcela:.2f} em {anos} parcelas")
else:
    print('O valor da parcela excede em 30% o valor do seu salário. Infelizmente não será possível realizar o empréstimo')