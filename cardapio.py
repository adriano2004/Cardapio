from time import sleep

sucos = ['Abacaxi', 'Abacaxi com hortelã', 'Abacaxi com hortelã e gengibre',
         'Acerola', 'Acerola com cenoura e laranja', 'Kiwi', 'Laranja', 'Laranja com acerola', 'Limão', 'Liminada Suíça', 'Limão com hortelã',
         'Melancia', 'Melancia com gengibre', 'Morango']

preco = [0, 7.00, 8.00, 8.50, 7.50, 8.50, 8.00, 7.50,
         7.50, 8.00, 7.00, 7.50, 7.00, 8.50, 9.00]

total = [0]


def cardapio():
    print("----------------------------------------------")
    print("|Escolha o(s) suco(s)                     ")
    print("----------------------------------------------")
    print("|1 | R$", preco[1], "|", sucos[0])
    print("----------------------------------------------")
    print("|2 | R$", preco[2], "|", sucos[1])
    print("----------------------------------------------")
    print("|3 | R$", preco[3], "|", sucos[2])
    print("----------------------------------------------")
    print("|4 | R$", preco[4], "|", sucos[3])
    print("----------------------------------------------")
    print("|5 | R$", preco[5], "|", sucos[4])
    print("----------------------------------------------")
    print("|6 | R$", preco[6], "|", sucos[5])
    print("----------------------------------------------")
    print("|7 | R$", preco[7], "|", sucos[6])
    print("----------------------------------------------")
    print("|8 | R$", preco[8], "|", sucos[7])
    print("----------------------------------------------")
    print("|9 | R$", preco[9], "|", sucos[8])
    print("----------------------------------------------")
    print("|10| R$", preco[10], "|", sucos[9])
    print("----------------------------------------------")
    print("|11| R$", preco[11], "|", sucos[10])
    print("----------------------------------------------")
    print("|12| R$", preco[12], "|", sucos[11])
    print("----------------------------------------------")
    print("|13| R$", preco[13], "|", sucos[12])
    print("----------------------------------------------")
    print("|14| R$", preco[14], "|", sucos[13])
    print("----------------------------------------------")


cardapio()
produtos = int(input("Digite o número do respectivo suco desejado:"))
quantidade = int(input("Quantidade: "))


def t(d, a): return d * a


def calculo():
    #print(t(quantidade, preco[produtos]))
    total.append(t(quantidade, preco[produtos]))


calculo()


def decisao():

    print("------------------------")
    print("| Continuar | Encerrar |")
    print("------------------------")
    opcao = input("Escolha uma opção: ")

    if opcao == "continuar" or opcao == "Continuar" or opcao == "c":
        cardapio()
        produtos = int(input("Digite o número do respectivo suco desejado2:"))
        quantidade = int(input("Quantidade: "))
        total.append(t(quantidade, preco[produtos]))
        decisao()
    elif opcao == "encerrar" or opcao == "Encerrar" or opcao == "e":
        print("Pedido encerrado")
        fim()
    else:
        print("OPÇÃO INVÁLIDA! Tente novamente")
        decisao()


def fim():
    soma = 0
    soma = sum(total)
    print("Total à pagar R$", soma)


decisao()


sleep(30)
