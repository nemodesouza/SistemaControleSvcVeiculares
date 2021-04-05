class TelaSistema:

    def tela_opcoes(self):
        print("")
        print("")
        print("====================================")
        print("------------------------------------")
        print("-------- SISTEMA DE CONTROLE -------")
        print("------ DE SERVIÇOS VEICULARES ------")
        print("------------------------------------")
        print("====================================")
        print("")
        print("")
        print("------- Selecione o assunto: -------")
        print("1 - Veiculos")
        print("2 - Revisao")
        print("3 - Clientes")
        print("0 - Sair")


        while True:
            try:
                opcao = int(input("Escolha a opção: "))

            except ValueError:
                print("Conteúdo Inválido. Digite o conteúdo correto.")
            else:
                return opcao

