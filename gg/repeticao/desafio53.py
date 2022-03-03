frase = str(input("Digite a palavra ou a frase a ser analisada: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#inverso = junto [::-1] -> usando fatiamento

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}")

if inverso == junto:
    print("temos um PALÍNDROMO!")
else:
    print("Não temos um PALÍNDROMO!")