import math
op = float(input("Informe o cateto oposto do triângulo: "))
adj = float(input("Informe o cateto adjacente do triângulo: "))
hyp = math.hypot(op,adj)

print(f"A hipotenusa do triângulo é de: {hyp}")