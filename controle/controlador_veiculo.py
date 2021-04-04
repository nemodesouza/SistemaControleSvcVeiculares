from limite.tela_veiculo import TelaVeiculo
from entidade.veiculo.veiculo import Veiculo 

class ControladorVeiculo():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_veiculo = TelaVeiculo()
        self.__veiculo = Veiculo

    def cadastrar_veiculo(self):
        dados_veiculo = self.__tela_veiculo.pega_dados_veiculo()

        veiculo = Veiculo(dados_veiculo["modelo"], dados_veiculo["ano"], dados_veiculo["placa"], 
        dados_veiculo["quilometragem"])

        self.__veiculo == veiculo

    def editar_veiculo(self):
        novo_modelo = input("Informe o novo modelo:")
        self.__veiculo.modelo = novo_modelo

        novo_ano = input("Informe o novo ano:")
        self.__veiculo.ano = novo_ano

        nova_placa = input("Informe a nova placa:")
        self.__veiculo.placa = nova_placa

        nova_quilometragem = input("Informe a nova quilometragem:")
        self.__veiculo.quilometragem = nova_quilometragem

        veiculo = Veiculo(novo_modelo, novo_ano, nova_placa, nova_quilometragem)
        self.__veiculo == veiculo

    def excluir_veiculo(self, veiculo):
        #del veiculo 
        pass   

    def mostrar_veiculo(self, veiculo):
        #self.__tela_veiculo.mostrar_dados(veiculo)
        pass 

    def voltar(self):
        pass
    
    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_veiculo, 2: self.editar_veiculo, 3: self.excluir_veiculo, 
        4: self.mostrar_veiculo, 5: self.voltar}

        lista_opcoes[self.__tela_veiculo.tela_opcoes()]()

