def mostralinha():
    print('-'*30)
def título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

#Programa principal
título('Curso em vídeo')
título('Python é muito bom!')


def soma(a, b):
    print(f'A = {a}, B = {b}')
    s = a + b
    print(f"A soma de A+B = {s}")
    
soma(4,5)
soma(8,9)
soma(2,1)
print()

#EMPACOTANDO E DESEMPACOTANDO
def contador(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números")

contador(5,7,3,1,4)
contador(8,4,7)

#DOBRANDO OS VALORES DE UMA LISTA
def dobra(valoresdobrados):
    pos = 0
    while pos<len(valoresdobrados):
        valoresdobrados[pos]*=2
        pos += 1


valores = [7,2,5,0,4]
dobra(valores)
print(valores)
