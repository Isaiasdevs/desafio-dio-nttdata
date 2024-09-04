# Desafio DIO-NTTData - Sistema Bancário em Python

import sys

saldo = 0
extrato = ''
menu=''
quantidade_saque=0


while menu !='Q':

    mensagem = print('''
        ############### Seja Bem-vindo(a) a DIO Bank! ###################

        Selecione a opção desejada.

        D - Depósito
        S - Saque
        E - Extrato
        Q - Sair

        ###################################################################
    ''')

    menu = input('\nDigite sua opção: ').upper()

    if menu == 'Q':
        sys.exit('Programa encerrado')

    if menu == 'D':
        
        valor = float(input('Informe o valor do depósito: '))

        if valor <=  0:
            print('Valor de depósito inválido.')
        else:
            saldo += valor
            extrato += f'\nDepósito: R$ {valor:.2f}'
            print(f'\nO depósito de R$ {valor:.2f} reais foi realizado com sucesso.\n')
        
    elif menu == 'S':

        if quantidade_saque > 3:
            print("Quantidade limite de saque atingida!")
        else:
             
             valor = float(input('Informe o valor do saque: '))

        if valor > saldo:
            print("Saldo insuficiente. Tente novamente!")
        elif valor > 500:
            print('Limite por saque ultrapassado.')
                    
        else:
            
            saldo -= valor
            extrato += f'\nSaque: R$ {valor:.2f}'
            quantidade_saque+= 1
            print(f'\nSaque de R$ {valor:.2f} reais realizado com sucesso.\n')
            
            
    elif menu == 'E':
        print(f'''
            ############### EXTRATO DE MOVIMENTAÇÕES ###############
                    {extrato}
                Saldo: {saldo:.2f}

            #######################################################
        ''')
    else:
        print('Opção inválida. Por favor, tente novamente.')






