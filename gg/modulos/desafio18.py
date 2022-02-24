import math
ang = int(input("Informe o valor do ângulo: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f"O seno, cosseno e tangente de {ang} são, respectivamente: {sen:.2f}, {cos:.2f} e {tan:.2f}")