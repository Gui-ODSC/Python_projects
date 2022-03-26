#Declaração de variáveis
valor = 0
lista_prod = ["Voltar", "Macarrão(R$ 5,99)", "Leite (R$ 4,56)",
"Arroz(R$ 7,20)", "Banana (R$ 4,50)", "Cerveja (R$ 3,50)", "Café (R$ 10,30)"]
lista_prec = [0, 5.99, 4.56, 7.20, 4.50, 3.50, 10.30]
lista_car = ["Voltar", "Lista de Produtos", "Valor Total"]
lista_de_escolhidos = []
lista_armazena = []
botao_voltar = True

while botao_voltar == True:
    print("Bem vindo/a ao menu, selecione uma opção: ")
    print("----- Menu -----")
    print("1 - Produtos")
    print("2 - Carrinho de Compras")
    print("3 - Finalizar Pedido")
    selecao_cliente = int(input("Escreva aqui o número da opção que deseja: "))

    #produtos
    if selecao_cliente == 1:
        for i in range(0, len(lista_prod)):
            print(i, "-",lista_prod[i])
        escolha_cliente = int(input("Escolha um produto digitando o número correspondente, ou digite 0 para voltar: "))
        if escolha_cliente > 0 and escolha_cliente <= 6:
            lista_de_escolhidos.append(escolha_cliente)
        while escolha_cliente > 0 and escolha_cliente <= 6:
            valor += (lista_prec[escolha_cliente])
            escolha_cliente = int(input("Escolha outro, ou digite 0 para voltar: "))
            if escolha_cliente > 0 and escolha_cliente <= 6:
                lista_de_escolhidos.append(escolha_cliente)
        if escolha_cliente != 0:
            print("Seus itens selecionados foram adicionados ao carrinho")
            botao_voltar = int(input("Digite 0 para voltar: "))
            botao_voltar = True
        if escolha_cliente == 0:
            print("Seus itens selecionados foram adicionados ao carrinho")
            botao_voltar = True
            
    #carrinho de compras
    if selecao_cliente == 2:
        for i in range(0, len(lista_car)):
            print(i, "-", lista_car[i])
        escolha_cliente2 = int(input("Selecione o número daquilo que deseja visualizar, ou digite 0 para voltar: "))
        if escolha_cliente2 == 0:
            botao_voltar = True
        if escolha_cliente2 == 1:
            for i in range(0, len(lista_de_escolhidos)):
                num_da_list = lista_de_escolhidos[i]
                print(lista_prod[num_da_list])
            if lista_de_escolhidos == [] :
                print("Lista Vazia")
                botao_voltar = int(input("Digite 0 para voltar: "))
                botao_voltar = True
            else:
                botao_voltar = int(input("Digite 0 para voltar: "))
                botao_voltar = True
            
        if escolha_cliente2 == 2:
            print("Valor total = R$%.2f" % (valor))
            botao_voltar = int(input("Digite 0 para voltar: "))
            botao_voltar = True
            
    #Finalizar Pedido
    if selecao_cliente == 3:
        print()
        print("<--Comprovante de Compra-->")
        print("           ...             ")
        for i in range(0, len(lista_de_escolhidos)):
                num_da_list = lista_de_escolhidos[i]
                print("    ",lista_prod[num_da_list])
        print("           ...             ")
        print("Valor pago = R$ %.2f" % (valor))
        valor = 0
        lista_de_escolhidos = []
        print("Seu carrinho agora esta vazio!")
        botao_voltar = False
