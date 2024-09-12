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
    
    opcao = input('\nDigite sua opção: ').upper()
    return opcao

def criar_usuario():
    print("\n=== Vamos criar seu usuário ===")
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento seguindo este modelo (dd/mm/aaaa): ")
    cpf = input("Informe o seu CPF (somente números): ")
    
    if verificar_usuario(cpf):
        print("CPF já cadastrado em nossa base.")
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
    print("\n=== Agora vamos criar sua conta ===")
    
    cpf = input("Nos informe o CPF do usuário: ")
    usuario_encontrado = verificar_usuario(cpf)
    
    if not usuario_encontrado:
        print("O usuário informado não foi encontrado. Cadastre o usuário primeiro.")
        return
    
    nova_conta = {
        'agencia': AGENCIA,
        'numero_conta': numero_conta,
        'usuario': usuario_encontrado
    }
    
    contas.append(nova_conta)
    numero_conta += 1

    print(f"Conta {nova_conta['numero_conta']} criada com sucesso para {usuario_encontrado['nome']}!")

def verificar_usuario(cpf):
    """Verifica se um usuário com o CPF informado existe na lista de usuários."""
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def verificar_conta(numero_conta):
    """Verifica se uma conta com o número informado existe na lista de contas."""
    for conta in contas:
        if conta['numero_conta'] == int(numero_conta):
            return conta
    return None

def depositar(saldo, extrato, /):
    print("\n=== Você selecionou a opção de depósito ===")
    
    numero_conta = input("Digite o número da conta para depósito: ")
    conta_encontrada = verificar_conta(numero_conta)
    
    if not conta_encontrada:
        print("Conta não localizada.")
        return saldo, extrato
    
    valor = float(input("Digite o valor do depósito: "))
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito na conta {numero_conta}: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso na conta {numero_conta}!")
    else:
        print("Valor de depósito inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, numero_saques, limite_saques):
    print("\n=== Você solicitou a opção de saque ===")

    numero_conta = input("Digite o número da conta para saque: ")
    conta_encontrada = verificar_conta(numero_conta)
    
    if not conta_encontrada:
        print("Erro: Conta não encontrada.")
        return saldo, extrato, numero_saques

    if numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")
    elif valor > 500:
        print("O valor do saque não pode ser superior a R$ 500.")
    elif valor > saldo:
        print("Saldo insuficiente.")
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
    
    numero_conta = input("Digite o número da conta para exibir o extrato: ")
    conta_encontrada = verificar_conta(numero_conta)
    
    if not conta_encontrada:
        print("Erro: Conta não encontrada.")
    else:
        print(f"Extrato da conta {numero_conta}:")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
    
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==============================")



