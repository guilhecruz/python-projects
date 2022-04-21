import sqlite3
import pyodbc

# Criando uma conexão com o banco de dados
server = 'sql-estudo.database.windows.net'
driver = '{ODBC Driver 17 for SQL Server}'
database = 'db-estudos'
username = 'guilherme.cruz@blueshift.com.br'
Authentication = 'ActiveDirectoryInteractive'
port = '1433'

# conn1 = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';AUTHENTICATION='+Authentication+';\
# PORT='+port+';DATABASE='+database+';UID='+username)  # +';PWD='+password)

conn = sqlite3.connect('lab02/guilhermecruz.db')

# Criando um cursor
c = conn.cursor()

# Criando a tabela de usuários


def table_usuario():
    c.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY,\
         nome TEXT, sobrenome TEXT, email TEXT, bairro TEXT, nascimento DATE)')

# Criando a tabela de cartão


def table_cartao():
    c.execute('CREATE TABLE IF NOT EXISTS cartao(id INTEGER PRIMARY KEY,\
        id_prop INTEGER, id_cartao INTEGER, creditos DOUBLE, tipo TEXT, emissao DATE)')

# Criando a tabela de Ônibus


def table_onibus():
    c.execute('CREATE TABLE IF NOT EXISTS onibus(id INTEGER PRIMARY KEY,\
        placa INTEGER, linha INTEGER, modelo TEXT, ano DATE, id_motorista INTEGER)')

# Criando a tabela de motoristas


def table_motoristas():
    c.execute('CREATE TABLE IF NOT EXISTS motoristas(id INTEGER PRIMARY KEY,\
        cnh INTEGER, nome TEXT, sobrenome TEXT, nascimento DATE)')

################### FIM DAS TABELAS #####################

# Criando método de leitura de todos os dados


def listar_usuarios():
    c.execute('SELECT * FROM usuarios')
    for linha in c.fetchall():
        print(linha)

# Métodos de leitura de atributos dos usuários


def listar_usuarios_nome():
    c.execute('SELECT * FROM usuarios ORDER BY nome')
    for linha in c.fetchall():
        print(linha[1])


def listar_usuarios_bairro():
    c.execute('SELECT * FROM usuarios ORDER BY bairro')
    for linha in c.fetchall():
        print(linha[4])

# Métodos de leitura dos atributos dos motoristas


def listar_motoristas_nome():
    c.execute('SELECT * FROM motoristas ORDER BY nome')
    for linha in c.fetchall():
        print(linha[2])


def listar_motoristas_cnh():
    c.execute('SELECT * FROM motoristas ORDER BY cnh')
    for linha in c.fetchall():
        print(linha[1])


def listar_onibus_modelo():
    c.execute('SELECT * FROM onibus ORDER BY modelo')
    for linha in c.fetchall():
        print(linha[3])


def listar_onibus_idmotorista():
    c.execute('SELECT * FROM onibus ORDER BY id_motorista')
    for linha in c.fetchall():
        print(linha[5])

# Método de leitura dos atributos de cartões
def listar_id_cartoes():
    c.execute('SELECT * FROM cartao ORDER BY id_cartao')
    for linha in c.fetchall():
        print(linha[2])


def listar_id_prop():
    c.execute('SELECT * FROM cartao ORDER BY id_prop')
    for linha in c.fetchall():
        print(linha[1])

# Criando métodos de adição

#   Adição de usuários
def adicionar_usuario(nome, sobrenome, email, bairro, nascimento):
    c.execute("INSERT INTO usuarios (nome, sobrenome, email, bairro, nascimento) VALUES (?, ?, ?, ?, ?)",
              (nome, sobrenome, email, bairro, nascimento))
    conn.commit()
   

#   Adição de motoristas
def adicionar_motorista(cnh, nome, sobrenome, nascimento):
    c.execute("INSERT INTO motoristas (cnh, nome, sobrenome, nascimento) VALUES (?, ?, ?, ?)",
              (cnh, nome, sobrenome, nascimento))
    conn.commit()

#   Adição de cartões
def adicionar_cartao(id_prop, id_cartao, creditos, tipo, emissao):
    c.execute("INSERT INTO cartao (id_prop, id_cartao, creditos, tipo, emissao) VALUES (?, ?, ?, ?, ?)",
              (id_prop, id_cartao, creditos, tipo, emissao))
    conn.commit()

#   Adição de ônibus 
def adicionar_onibus(placa, linha, modelo, ano, id_motorista):
    c.execute("INSERT INTO onibus (placa, linha, modelo, ano, id_motorista) VALUES (?, ?, ?, ?, ?)",
              (placa, linha, modelo, ano, id_motorista))
    conn.commit()


# Executando métodos de criação de tabelas
table_usuario()
table_cartao()
table_onibus()
table_motoristas()
