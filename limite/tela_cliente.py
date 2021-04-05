class TelaCliente:

    def tela_opcoes(self):
        print("")
        print("")
        print("====================================")
        print("============== CLIENTE =============")
        print("====================================")
        print("")
        print("------- Selecione o assunto: -------")
        print("")
        print("1 - Cadastrar Cliente")
        print("2 - Remover Cliente")
        print("3 - Editar Cliente")
        print("4 - Listar Clientes")
        print("5 - Pesquisar Cliente pelo Nome")
        print("0 - Voltar")
        print("")
        print("")

        opcao = int(input("Escolha a opcao:"))
        return opcao