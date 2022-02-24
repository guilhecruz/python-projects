#6 primeiros elementos da string espaçados de 2 em 2
frase[0:5:2]
#obtem o tamanho da string
len(frase)
#conta quantos elementos solicitados contem na string entre a posição 0 e a posição 13
frase.count("o", 0, 13)
#acha o elemento solicitado dentro da string
frase.find("deo")
#apenas diz se existe o elemento na string
"curso" in frase
#substitui o elemento dentro da string
frase.replace("python","android")
#Transforma todas os caracteres em maiúsculas
frase.upper()
#Transforma todas os caracteres em minúsculas
frase.lower()
#Transforma todas os caracteres em minúsculo, menos a primeira letra
frase.capitalize()
#Transforma todos os caracteres iniciais em maiúsculo
frase.title()
#Retira todos os espaços inuteis digitados
frase.strip()
#Retira os espaços livres da direita
frase.rstrip()
#retira os espaços livres da esquerda
frase.lstrip()
#Cria uma divisão na string, gerando novas indexações e novas strings
frase.split()
#Junta as strings usando - como separador entre as strings
'-'.join(frase)