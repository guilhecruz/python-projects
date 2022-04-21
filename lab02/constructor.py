import sqlite3


# Criando uma conexão com o banco de dados
conn = sqlite3.connect('guilhermecruz.db')

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


def leitura_usuarios():
    c.execute('SELECT * FROM usuarios')
    for linha in c.fetchall():
        print(linha)


# Criando métodos de adição
def adicionar_usuario(nome, sobrenome, email, bairro, nascimento):
    c.execute("INSERT INTO usuarios (nome, sobrenome, email, bairro, nascimento) VALUES (?, ?, ?, ?, ?)",
              (nome, sobrenome, email, bairro, nascimento))
    conn.commit()
    # c.close()


def adicionar_motorista(cnh, nome, sobrenome, nascimento):
    c.execute("INSERT INTO motoristas (cnh, nome, sobrenome, nascimento) VALUES (?, ?, ?, ?)",
              (cnh, nome, sobrenome, nascimento))
    conn.commit()


def adicionar_cartao(id_prop, id_cartao, creditos, tipo, emissao):
    c.execute("INSERT INTO cartao (id_prop, id_cartao, creditos, tipo, emissao) VALUES (?, ?, ?, ?, ?)",
              (id_prop, id_cartao, creditos, tipo, emissao))
    conn.commit()


def adicionar_onibus(placa, linha, modelo, ano, id_motorista):
    c.execute("INSERT INTO onibus (placa, linha, modelo, ano, id_motorista) VALUES (?, ?, ?, ?, ?)",
              (placa, linha, modelo, ano, id_motorista))
    conn.commit()


# Executando métodos de criação de tabelas
table_usuario()
table_cartao()
table_onibus()
table_motoristas()
