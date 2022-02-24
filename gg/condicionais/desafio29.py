vel = int(input("Qual a velocidade medida?"))

if vel > 80:
    multa = (vel - 80) * 7
    print(f"Você foi multado por excesso de velocidade e deverá pagar R$ {multa}")
else:
    print("Sua velocidade estava dentro do limite permitido")