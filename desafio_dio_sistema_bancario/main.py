
from funcoes import exibir_menu, criar_usuario, criar_conta, depositar, sacar, exibir_extrato

def main():

    saldo = 0
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    
    while True:
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
            break

        else:
            print("Opção inválida. Tente novamente.")


main()



