km = float(input("Informe quantos km foram rodados com o veículo:"))
dias = int(input("Informe quantos dias você passou com om veículo:"))

preco = (km*0.15) + (dias *60)

print(f"O valor que deve ser pago do aluguel é de R${preco}")