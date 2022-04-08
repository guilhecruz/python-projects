import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mERRO: Não foi possível acessar o site.\033[m')
else:
    print('\033[0;32mO site foi acessado com sucesso.\033[m')