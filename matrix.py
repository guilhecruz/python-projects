from matplotlib import pyplot, colors
class Bus:

    def __init__(self, rows, columns):
        self.rsize = rows
        self.csize = columns
        self.assentos_livres = 28
        self.matrix = [[0 for _ in range(self.csize)] for _ in range(self.rsize)]
        self.tickets_bought = 0
        print(self.matrix)

    def compra_passagem(self):
        while self.assentos_livres >= 0: 
            print("Bem vindo a empresa PoccoBus, uma das maiores empresas de transporte do país!")
            passagens = int(input("Digite quantas passagens você deseja comprar:"))
            print("Muito obrigado por escolher a PoccoBus")
            
            if passagens > self.assentos_livres:
                print("Infelizmente, a quantidade de tickets que você soliciou não está mais disponível")
            else:
                self.assentos_livres = self.assentos_livres - passagens
                self.tickets_bought = self.tickets_bought + passagens
                print(f"Compra efetuada com sucesso!\nAssentos disponíveis: {self.assentos_livres}")
                self.book_chairs(passagens)
                self.plot_graphic()
                self.export_file()
                # print(self.matrix)
                
            
        print(self.assentos_livres)

    def export_file(self):
        f = open("result.txt", "a")
        f.write(f"Passagens vendidas: {self.tickets_bought}\nPassagens disponíveis: {self.assentos_livres}\n=======\n")
        f.close()

    def plot_graphic(self):
        colormap = colors.ListedColormap(["red","green"])
        pyplot.figure(figsize=(5,5))
        pyplot.imshow(self.matrix,
                        cmap=colormap)
        pyplot.show()
    
    def book_chairs(self, passagens):
        for _ in range(0,passagens):
            self.fill_matrix()

    def fill_matrix(self):
        for i in range(0,self.rsize):
            for j in range(0,self.csize):
                if self.matrix[i][j] == 0:
                    self.matrix[i][j] = 1
                    return
        print("There is no chair left to book!!!!")

Bus(7,4).compra_passagem()