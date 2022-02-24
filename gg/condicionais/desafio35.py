a1 = int(input("Primeiro segmento:"))
a2 = int(input("Segundo segmento: "))
a3 = int(input("Terceiro segmento: "))

a4 = a2 + a3
a5 = a1 + a3
a6 = a1 + a2

print(f"Os segmentos submetidos foram {a1}, {a2} e {a3}")

if a1 < a4 and a2 < a5 and a3 < a6:
    print(f"Os angulos {a1}, {a2} e {a3}, satisfazem as condições para criação de um triângulo")
else:
    print(f"Os angulos {a1}, {a2} e {a3} não satisfaem as condições para a criação de um triângulo")