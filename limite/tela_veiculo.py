class TelaVeiculo():

    def tela_opcoes(self):
        print("-------- Veiculo ---------")
        print("Escolha sua opcao")
        print("1 - Criar veiculo")
        print("2 - Editar veiculo")
        print("3 - Excluir veiculo")
        print("4 - Mostrar veiculo")
        print("5 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_veiculo(self):
        print("-------Incluir Veiculo-------")
        modelo = input("Modelo: ")
        ano = input("Ano: ")
        placa = input("Placa: ")
        quilometragem = input("Quilometragem: ")

        return {"modelo": modelo, "ano": ano, "placa": placa, "quilometragem": quilometragem}

    def mostrar_dados(self, veiculo):
        print("Modelo do veiculo: ", veiculo.modelo)
        print("Ano do veiculo: ", veiculo.ano)
        print("Placa do veiculo: ", veiculo.placa)
        print("Quilometragem do veiculo: ", veiculo.quilometragem)