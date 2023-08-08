def menu():
    print("----------MENU----------")
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Visualizar extrato")
    print("0 - Sair")

def programa():
    saque = []
    deposito = []
    saldo = 0
    limite_diario = 3
    while True:
        print(menu())
        opcao = int(input("Selecione a opção desejada: "))
        if opcao == 1:
            if limite_diario <= 3:
                x = int(input("Digite o valor que deseja sacar: R$ "))
                if x <= saldo and x <= 500:
                    saldo -= x
                    limite_diario -= 1
                    saque.append(x)
                    print("Saque realizado!")
                elif x > saldo:
                    print("Saldo insuficiente.")
                elif x > 500:
                    print("Seu limite é de R$ 500,00 por saque.")
                else:
                    print("Você atingiu o limite diário de saques.")

        if opcao == 2:
            y = int(input("Digite o valor que deseja depositar: R$ "))
            if y > 0:
                saldo += y
                deposito.append(y)
                print("Valor depositado!")
            else:
                print("Não é possível depositar este valor.")

        if opcao == 3:
            print("Depósitos realizados: {}" .format(deposito))
            print("Saques realizados: {}".format(saque))
            print("Saldo total: R$ {}".format(saldo))

        if opcao == 0:
            print("Saindo...")
            exit()

        if opcao >= 4:
            print("Opção inválida!")

programa()