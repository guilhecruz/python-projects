brasileirao = ('Corinthians','Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f"Lista de times do Brasileirão: {brasileirao}")

print(f"Os cinco primeiro times são {brasileirao[0:5]}")
print(f"Os quatro últimos são {brasileirao[-4:]}")
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print(f'O Chapecoense está na {brasileirao.index("Chapecoense")+1}ª Posição')
