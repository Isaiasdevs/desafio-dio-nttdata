import sys

saldo = 0
extrato = ''
#quantidade_saque=0
usuarios = []
contas = []
numero_conta = 1  # Inicializando o número da conta

AGENCIA = '0001'

def exibir_menu():
    print('''
    ############### Seja Bem-vindo(a) ao DIO Bank! ###################

    Selecione a opção desejada.
    A - Abrir conta
    D - Depositar
    E - Extrato
    S - Sacar
    Q - Sair

    ###################################################################
    ''')
    
    # Captura e retorna a opção escolhida pelo usuário
    opcao = input('\nDigite sua opção: ').upper()
    return opcao

def criar_usuario():
    print("\n=== Criar Usuário ===")
    
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cpf = input("CPF (somente números): ")
    
    # Verifica se o CPF já está cadastrado para outro usuário
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: CPF já cadastrado.")
            return
    
    endereco = input("Endereço (logradouro, nro, bairro, cidade/sigla estado): ")
    
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")


def criar_conta():
    global numero_conta
    print("\n=== Criação de Conta ===")
    
    cpf = input("Informe o CPF do usuário: ")

    # Busca o usuário com o CPF fornecido
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("Erro: Usuário não encontrado. Cadastre o usuário primeiro.")
        return

    # Cria a conta e associa ao usuário
    nova_conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario_encontrado
    }

    # Adiciona a conta na lista global de contas
    contas.append(nova_conta)
    numero_conta += 1  # Incrementa o número da conta para a próxima conta

    print(f"Conta {nova_conta['numero_conta']} criada com sucesso para {usuario_encontrado['nome']}!")


def depositar(saldo, extrato, /):
    print("\n=== Depósito ===")
    
    # Solicita e valida o número da conta
    numero_conta = input("Digite o número da conta para depósito: ")
    conta_encontrada = None
    
    for conta in contas:
        if conta['numero_conta'] == int(numero_conta):
            conta_encontrada = conta
            break
    
    if not conta_encontrada:
        print("Erro: Conta não encontrada.")
        return saldo, extrato
    
    # Solicita e valida o valor do depósito
    valor = float(input("Digite o valor do depósito: "))
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito na conta {numero_conta}: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso na conta {numero_conta}!")
    else:
        print("Erro: O valor do depósito deve ser positivo.")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, numero_saques, limite_saques):
    print("\n=== Saque ===")

    # Solicita e valida o número da conta
    numero_conta = input("Digite o número da conta para saque: ")
    conta_encontrada = None
    
    for conta in contas:
        if conta['numero_conta'] == int(numero_conta):
            conta_encontrada = conta
            break
    
    if not conta_encontrada:
        print("Erro: Conta não encontrada.")
        return saldo, extrato, numero_saques

    if numero_saques >= limite_saques:
        print("Erro: Limite de saques diários atingido.")
    elif valor > 500:
        print("Erro: O valor do saque não pode ser superior a R$ 500.")
    elif valor > saldo:
        print("Erro: Saldo insuficiente.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque na conta {numero_conta}: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso na conta {numero_conta}!")
    else:
        print("Erro: O valor do saque deve ser positivo.")
    
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, *, extrato):
    print("\n=== Extrato ===")
    
    # Solicita e valida o número da conta
    numero_conta = input("Digite o número da conta para exibir o extrato: ")
    conta_encontrada = None
    
    for conta in contas:
        if conta['numero_conta'] == int(numero_conta):
            conta_encontrada = conta
            break
    
    if not conta_encontrada:
        print("Erro: Conta não encontrada.")
    else:
        print(f"Extrato da conta {numero_conta}:")
        if not extrato:  # Se o extrato estiver vazio
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
    
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==============================")


