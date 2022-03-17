def calcarea(altura, largura):
    print(f'A altura foi de {altura} e a largura de {largura}m²')
    area = altura * largura
    print(f'A área total foi de {area}')

def cabeçalho():
    print("Controle de Terrenos")
    print('-'*30)

cabeçalho()
altura = float(input("forneça a altura: "))    
largura = float(input("forneça a largura: "))
calcarea(altura, largura)
