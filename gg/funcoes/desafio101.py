def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA')
    elif 16 <= idade < 18 or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')

ano = int(input("Qual o seu ano de nascimento? "))
voto(ano)