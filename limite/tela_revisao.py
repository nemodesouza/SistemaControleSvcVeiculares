class TelaRevisao():

    def tela_opcoes(self):
        print("-------- Revisao ---------")
        print("Escolha sua opcao")
        print("1 - Iniciar revisao")
        print("2 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def listar_revisoes(self, lista_substituicoes, lista_verificacoes):

        for i in lista_substituicoes:
            print("[  ] ", i.descricao)
        
        print("----------------------")

        for v in lista_verificacoes:
            print("[  ] ", v.descricao)
        
