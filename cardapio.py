from time import sleep

sucos = ['Abacaxi', 'Abacaxi com hortelã', 'Abacaxi com hortelã e gengibre',
         'Acerola', 'Acerola com cenoura e laranja', 'Kiwi', 'Laranja', 'Laranja com acerola', 'Limão', 'Liminada Suíça', 'Limão com hortelã',
         'Melancia', 'Melancia com gengibre', 'Morango']


def cardapio():
    print("----------------------------------------------")
    print("|Escolha o(s) suco(s)                     ")
    print("----------------------------------------------")
    print("|1 | R$ 7,99 |", sucos[0])
    print("----------------------------------------------")
    print("|2 | R$ 8,20 |", sucos[1])
    print("----------------------------------------------")
    print("|3 | R$ 8,50 |", sucos[2])
    print("----------------------------------------------")
    print("|4 | R$ 7,99 |", sucos[3])
    print("----------------------------------------------")
    print("|5 | R$ 8,50 |", sucos[4])
    print("----------------------------------------------")
    print("|6 | R$ 7,99 |", sucos[5])
    print("----------------------------------------------")
    print("|7 | R$ 7,50 |", sucos[6])
    print("----------------------------------------------")
    print("|8 | R$ 7,50 |", sucos[7])
    print("----------------------------------------------")
    print("|9 | R$ 8,50 |", sucos[8])
    print("----------------------------------------------")
    print("|10| R$ 7,99 |", sucos[9])
    print("----------------------------------------------")
    print("|11| R$ 7,70 |", sucos[10])
    print("----------------------------------------------")
    print("|12| R$ 7,99 |", sucos[11])
    print("----------------------------------------------")
    print("|13| R$ 8,20 |", sucos[12])
    print("----------------------------------------------")
    print("|14| R$ 8,99 |", sucos[13])
    print("----------------------------------------------")


cardapio()
produtos = int(input("Digite o número do respectivo suco desejado:"))


def decisao():

    print("------------------------")
    print("| Continuar | Encerrar |")
    print("------------------------")
    opcao = input("Escolha uma opção: ")

    if opcao == "continuar" or opcao == "Continuar":
        cardapio()
        produtos = int(input("Digite o número do respectivo suco desejado2:"))
        loop()

    elif opcao == "encerrar" or opcao == "Encerrar":
        print("Pedido encerrado")

    else:
        print("OPÇÃO INVÁLIDA! Tente novamente")
        decisao()


def loop():
    decisao()


loop()
sleep(30)
