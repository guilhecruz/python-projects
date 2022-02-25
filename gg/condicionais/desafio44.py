valor = float(input("Qual o valor do produto? "))
pag = int(input("Informe a forma de pagamento:\n 1 - à vista \n 2 - à vista no cartão \n 3 - 2x no cartão \n 4 - 3x ou mais no cartão "))


if pag == 1:
    pag = valor - (valor*0.10)
    print(f"O valor do produto com disconto é de {pag}")
if pag == 2:
    pag = valor - (valor*0.05)
    print(f"O valor do produto com disconto é de {pag}")
if pag == 3:
    print(f"O valor do produto é de {valor}")
if  pag == 4:
    pag = valor - (valor*0.20)
    print(f"O valor do produto é de {pag}")        
