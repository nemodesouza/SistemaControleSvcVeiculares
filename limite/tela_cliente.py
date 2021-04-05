class TelaCliente:

    def tela_opcoes(self):
        #exibe as informações da tela de cliente
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

        opcao = int(input("Escolha a opção: "))
        return opcao

    def coleta_dados_pessoa_fisica(self):
        # coleta dados de cliente pessoa física
        print("Abrir tela pra coletar dados Pessia Física")
        print("-------- Cadastrar Cliente ---------")
        print("----------- PESSOA FÍSICA ----------")
        
        #gera o código automaticamente (verificar como fazer isso"
        codigo = input("Defina um Código para o Cliente: ")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        data_nascimento = input("Data de Nascimento: ")
        cpf = input("CPF: ")
        rg = input("R.G.: ")
        orgao_emissor = input("Órgão Emissor: ")
        veiculo = input("Veículo: ")

        return {"codigo":codigo, "nome": nome, "telefone": telefone, "endereco": endereco, "data_nascimento": data_nascimento, "cpf": cpf, "rg": rg, "orgao_emissor": orgao_emissor, "veiculo": veiculo}

    def coleta_dados_pessoa_juridica(self):
        # coleta dados de cliente pessoa jurídica
        print("Abrir tela pra coletar dados Pessia Física")

    def tipo_de_cliente(self):
        # escolhe se é cliente pessoa física ou jurídica
        print("")
        print("--- Selecione o tipo de cliente: ---")
        print("")
        print("1 - Pessoa Física")
        print("2 - Pessoa Jurídica")
        print("0 - Voltar")
        print("")
        print("")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def listar_clientes(self, dados_cliente):
        print("CÓDICO CLIENTE: ", dados_cliente["codigo"])
        print("NOME CLIENTE: ", dados_cliente["nome"])
        print("FONE CLIENTE: ", dados_cliente["telefone"])
        print("END CLIENTE: ", dados_cliente["endereco"])
        print("DATA NASC.: ", dados_cliente["data_nascimento"])
        print("CPF: ", dados_cliente["cpf"])
        print("R.G.: ", dados_cliente["rg"])
        print("ÓRGÃO EMISSOR: ", dados_cliente["orgao_emissor"])
        print("VEÍCULO: ", dados_cliente["veiculo"])