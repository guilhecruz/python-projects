import constructor
from termcolor import colored


def cabecalho():
    print('-' * 50)
    print(colored('{:^50}'.format(
        'Seja bem vindo ao Banco de Dados POCCOBUS'), 'blue'))
    print('-' * 50)


def menu():
    print('-' * 50)
    print(colored('{:^50}'.format('Menu'), 'green'))
    print('-' * 50)
    print(colored('1 - Cadastro', 'yellow'))
    print(colored('2 - Exibição', 'yellow'))
    print(colored('3 - História da Pocco Bus', 'yellow'))
    print(colored('4 - Sair', 'yellow'))
    print('-' * 50)
    e = int(
        input(colored('{:^50}'.format('O que você deseja fazer? '), 'blue')))
    if e == 1:
        menu_cadastro()
    elif e == 2:
        menu_exibir()
    elif e == 3:
        historia()
    elif e == 4:
        print('-' * 50)
        print(colored('{:^50}'.format(
            'Obrigado por usar o Banco de Dados POCCOBUS'), 'blue'))
        print('-' * 50)
        exit()
    else:
        print('-' * 50)
        print(colored('{:^50}'.format('Opção inválida'), 'red'))
        print('-' * 50)
        menu()


def menu_cadastro():
    print('-' * 50)
    print(colored('{:^50}'.format('O que você deseja cadastrar '), 'blue'))
    print('-' * 50)
    print(colored('1 - Usuários', 'yellow'))
    print(colored('2 - Motoristas', 'yellow'))
    print(colored('3 - Ônibus', 'yellow'))
    print(colored('4 - Cartões', 'yellow'))
    print(colored('5 - Voltar', 'yellow'))

    print('-' * 50)
    e = input(colored('{:^50}'.format('Digite sua escolha: '), 'blue'))
    if e == '1':
        cadastrar_usuario()
        menu()
    elif e == '2':
        cadastrar_motorista()
        menu()
    elif e == '3':
        cadastrar_onibus()
        menu()
    elif e == '4':
        cadastrar_cartao()
        menu()
    elif e == '5':
        menu()
    else:
        print('-' * 50)
        print(colored('{:^50}'.format('Opção inválida'), 'red'))
        print('-' * 50)
        menu_cadastro()


def menu_exibir():
    print('-' * 50)
    print('-' * 50)
    print(colored('1 - Usuários', 'yellow'))
    print(colored('2 - Motoristas', 'yellow'))
    print(colored('3 - Ônibus', 'yellow'))
    print(colored('4 - Cartões', 'yellow'))
    print(colored('5 - Voltar', 'yellow'))
    e = input(colored('{:^50}'.format('O que você deseja exibir? '), 'blue'))
    if e == '1':
        listar_usuarios()
    elif e == '2':
        listar_motoristas()
    elif e == '3':
        listar_onibus()
    elif e == '4':
        listar_cartoes()
    elif e == '5':
        menu()
    else:
        print('-' * 50)
        print(colored('{:^50}'.format('Opção inválida'), 'red'))
        print('-' * 50)
        menu_exibir()


def cadastrar_usuario():
    print('-' * 50)
    print(colored('{:^50}'.format('Cadastro de Usuário'), 'blue'))
    print('-' * 50)
    nome = str(input(colored('Nome: ', 'yellow')))
    sobrenome = str(input(colored('Sobrenome: ', 'yellow')))
    email = str(input(colored('Email: ', 'yellow')))
    bairro = str(input(colored('Bairro: ', 'yellow')))
    nascimento = input(colored('Nascimento: ', 'yellow'))
    constructor.c.execute('INSERT INTO usuarios (nome, sobrenome, email, bairro, nascimento) VALUES (?, ?, ?, ?, ?)',
                          (nome, sobrenome, email, bairro, nascimento))
    constructor.conn.commit()
    print('-' * 50)
    print(colored('{:^50}'.format('Usuário cadastrado com sucesso!'), 'green'))
    print('-' * 50)
    cabecalho()
    menu()


def cadastrar_motorista():
    print('-' * 50)
    print(colored('{:^50}'.format('Cadastrar Motorista'), 'blue'))
    print('-' * 50)
    cnh = int(input(colored('CNH: ', 'yellow')))
    nome = str(input(colored('Nome: ', 'yellow')))
    sobrenome = str(input(colored('Sobrenome: ', 'yellow')))
    nascimento = str(input(colored('Nascimento: ', 'yellow')))
    constructor.c.execute(
        'INSERT INTO motoristas (cnh, nome, sobrenome, nascimento) VALUES (?, ?, ?, ?)', (cnh, nome, sobrenome, nascimento))
    constructor.conn.commit()
    print('-' * 50)
    print('{:^50}'.format('Motorista cadastrado com sucesso!'))
    print('-' * 50)
    cabecalho()
    menu()


def cadastrar_onibus():
    print('-' * 50)
    print('{:^50}'.format('Cadastrar Ônibus'))
    print('-' * 50)
    placa = int(input(colored('Placa: ', 'yellow')))
    linha = int(input(colored('Linha: ', 'yellow')))
    modelo = str(input(colored('Modelo: ', 'yellow')))
    ano = int(input(colored('Ano: ', 'yellow')))
    id_motorista = int(input(colored('ID Motorista: ', 'yellow')))
    constructor.c.execute('INSERT INTO onibus (placa, linha, modelo, ano, id_motorista) VALUES (?, ?, ?, ?, ?)',
                          (placa, linha, modelo, ano, id_motorista))
    constructor.conn.commit()
    print('-' * 50)
    print(colored('{:^50}'.format('Ônibus cadastrado com sucesso!'), 'green'))
    print('-' * 50)
    cabecalho()
    menu()


def cadastrar_cartao():
    print('-' * 50)
    print(colored(('{:^50}'.format('Cadastrar Cartão')), 'blue'))
    print('-' * 50)
    id_prop = int(input(colored("ID do proprietário: ", 'yellow')))
    id_cartao = int(input(colored('ID do cartão: ', 'yellow')))
    creditos = float(input(colored("Créditos: ", 'yellow')))
    tipo = str(input(colored('Tipo(comum, estudante, vale ou idoso): ', 'yellow')))
    emissao = str(input(colored('Data de emissão: ', 'yellow')))
    constructor.c.execute(
        'INSERT INTO cartao (id_prop, id_cartao, creditos, tipo, emissao) VALUES (?, ?, ?, ?, ?)',
        (id_prop, id_cartao, creditos, tipo, emissao))
    constructor.conn.commit()
    print('-' * 50)
    print(colored('{:^50}'.format('Cartão cadastrado com sucesso!'), 'green'))
    print('-' * 50)
    cabecalho()
    menu()


def listar_usuarios():
    print('-' * 50)
    print(colored('{:^50}'.format('Listar Usuários'), 'blue'))
    print('-' * 50)
    constructor.c.execute('SELECT * FROM usuarios')
    for linha in constructor.c:
        print(linha)
    print('-' * 50)
    cabecalho()
    menu()


def listar_motoristas():
    print('-' * 50)
    print(colored('{:^50}'.format('Listar Motoristas'), 'blue'))
    print('-' * 50)
    constructor.c.execute('SELECT * FROM motoristas')
    for linha in constructor.c:
        print(linha)
    print('-' * 50)
    cabecalho()
    menu()


def listar_onibus():
    print('-' * 50)
    print(colored('{:^50}'.format('Listar Ônibus'), 'blue'))
    print('-' * 50)
    constructor.c.execute('SELECT * FROM onibus')
    for linha in constructor.c:
        print(linha)
    print('-' * 50)
    cabecalho()
    menu()


def listar_cartoes():
    print('-' * 50)
    print(colored('{:^50}'.format('Listar Cartão'), 'blue'))
    print('-' * 50)
    constructor.c.execute('SELECT * FROM cartao')
    for linha in constructor.c:
        print(linha)
    print('-' * 50)
    cabecalho()
    menu()


def historia():
    print('-' * 50)
    print(colored("A POCCOBUS é uma empresa de ônibus especializada em viagens intermunicipais, com foco no conforto e qualidade nos serviços prestados aos seus passageiros.\
Uma empresa fundada em 1993, hoje já possui um grande reconhecimento no mercado, com mais de 20 anos de experiência no mercado de transporte público.\
Premiada consecutivas vezes pelas revistas Times e Forbs, a POCCOBUS é referência no segmento de transporte público, com mais de 100 mil passageiros em todo o país.\
Vem fazer parte da família POCCOBUS. Estamos pronto para lhe receber da melhor maneira possível.", 'blue'))
    menu()
