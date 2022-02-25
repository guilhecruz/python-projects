peso = float(input("Qual é o seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (m) "))
imc = peso / (altura**2)

print(f"O IMC dessa pessoa é de {imc:.1f}")

if imc <= 18.5:
    print("Você está abaixo do seu peso ideal")
elif imc <= 25:
    print("Você está na sua faixa de peso ideal")
elif imc <= 30:
    print("Você está com sobrepeso")
elif imc <=40:
    print("Você está com obesidade grau 1")
else:
    print("Você está com obesidade mórbida")