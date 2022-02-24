d = int(input("Qual a distância do seu destino em km? "))

if d <= 200:
    d = d*0.50
    print(f"A sua viagem custará R${d} reais")
if d > 200:
    d = d*0.45
    print(f"A sua viagem custará R${d} reais")