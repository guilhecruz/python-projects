from datetime import date


ano = int(input("Que ano quer analisar? Coloque 0 para selecionar o ano atual "))

if ano == 0:
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 1 and ano % 400 == 0:
    print(f"O ano {ano} é um ano bissexto")
else:
    print(f"O ano {ano} não é um ano bissexto")




