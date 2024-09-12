# Código desafio dio NTTData
# Simualação de ums sistema bancários com algumas funções básicas. 


from funcoes import exibir_menu, criar_usuario, criar_conta, depositar, sacar, exibir_extrato # arquivos foram separados para que fiquem mais organizados e de fácil manutenção. Sendo assim se faz necessária a importação das funções que serão utilizadas. 

def main(): #função principal responsável por fazer o sistema rodar e pela chamada das respectivias funções. 

    saldo = 0
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    
    while True: # Laço necessário para que o programa fique em loop até que a opção do menu seja escolhida. 
        opcao = exibir_menu()

        if opcao == 'A':
            criar_usuario()
            criar_conta()

        elif opcao == 'D':
            saldo, extrato = depositar(saldo, extrato)
        
        elif opcao == 'S':
            valor_saque = float(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, 
                valor=valor_saque, 
                extrato=extrato, 
                numero_saques=numero_saques, 
                limite_saques=limite_saques
            )

        elif opcao == 'E':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'Q':
            print("Obrigado por utilizar o DIO Bank! Até logo.")
            break #encerra o sistema

        else:
            print("Opção inválida. Tente novamente.") #Em resposta a qualquer opção diferente da informada no menu


main() # chamada da função main para que o programa dê inicio. 



