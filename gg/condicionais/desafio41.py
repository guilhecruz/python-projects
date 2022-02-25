from datetime import date

ano = int(input("Qual o ano de nascimento do atleta? "))
id = date.today().year - ano

if id <= 9:
    print("O competidor entrará na categoria MIRIM")
elif id <=14:
    print("O competidor entrará na categoria INFANTIL")
elif id <=19:
    print("O competidor entrará na categoria JUNIOR")
elif id <=20:
    print("O competidor entrará na categoria SENIOR")
else:
    print("O competidor entrará na categoria MASTER")
