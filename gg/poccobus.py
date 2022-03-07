from matplotlib import pyplot, colors
import emoji
from time import sleep

class Bus:

#Definimos o número de assentos livres e criamos uma matriz para visualização dos assentos em forma binária (0,1)
    def __init__(self, rows, columns):
        self.rsize = rows
        self.csize = columns
        self.assentos_livres = rows*columns
        self.matrix = [[0 for _ in range(self.csize)] for _ in range(self.rsize)]
        self.tickets_bought = 0
        print(self.matrix)

#Boas vindas na execução do código e input de quantas passagens o usuário deseja comprar
    def compra_passagem(self):
        while self.assentos_livres >= 0: 
            print(emoji.emojize("Bem vindo a empresa PoccoBus, uma das maiores empresas de transporte do país!:earth_americas: :bus:", use_aliases=True))
            passagens = int(input("Digite quantas passagens você deseja comprar:"))
            print("-=-"*20)
            print("Verificando a quantidade de assentos disponíveis...")
            print("-=-"*20)
            sleep(1.5)
            print("Muito obrigado por escolher a PoccoBus")

#Condicionais que devem ser satisfeitos. Se o número de passagens solicitadas for maior que o número de assentos livres,
#não será possível comprar o número solicitado e é mostrada a quantidade de assentos livres.          
            if passagens > self.assentos_livres:
                print(f"Infelizmente, a quantidade de tickets que você soliciou não está mais disponível. O número de passagens disponíveis é de {self.assentos_livres}")
#Aqui é subtraído a quantidade de passagens que o usuário comprou da quantidade de assentos livres
#e é mostrada uma mensagem de agradecimento, seguida da quantidade de assentos disponíveis atualizada
            else:
                self.assentos_livres = self.assentos_livres - passagens
                self.tickets_bought = self.tickets_bought + passagens
                print(f"Compra efetuada com sucesso!\nAssentos disponíveis: {self.assentos_livres}")
#Chamamos as funções de reservas, gráfico e txt
                self.reservas(passagens)
                self.grafico()
                self.txt()

        print(self.assentos_livres)
#Aqui exportamos o arquivo txt contendo as informações de quantas passagens foram vendidas e quantos assentos ainda restam
#a cada excução do programa
    def txt(self):
        f = open("resultado.txt", "a")
        f.write(f"Passagens vendidas: {self.tickets_bought}\nPassagens disponíveis: {self.assentos_livres}\n=======\n")
        f.close()
#Função que plota o gráfico dos assentos preenchidos (vermelhos) e os assentos livres (verdes) em uma matriz (7,4)
    def grafico(self):
        colormap = colors.ListedColormap(["green","red"])
        pyplot.figure(figsize=(5,5))
        pyplot.imshow(self.matrix,
                        cmap=colormap)
        pyplot.show()
#Função que define quantos assentos serão preenchidos na matriz, com base no número de passagens compradas
    def reservas(self, passagens):
        for _ in range(0,passagens):
            self.preenche_matriz()
#Função que percorre a matriz, procurando o próximo assento livre (0) e substituindo o valor binário por 1.
#Caso não haja mais assentos livres, é mostrada a mensagem de que não há mais assentos disponíveis
    def preenche_matriz(self):
        for i in range(0,self.rsize):
            for j in range(0,self.csize):
                if self.matrix[i][j] == 0:
                    self.matrix[i][j] = 1
                    return
        print("Já não há mais assentos disponíveis para esta viagem!!!")

#Aqui é onde rodamos a classe "Bus" com o número de linhas e colunas que queremos 
Bus(7,4).compra_passagem()