from limite.tela_sistema import TelaSistema
from controle.controlador_veiculo import ControladorVeiculo
from controle.controlador_cliente import ControladorCliente
from controle.controlador_relatorio import ControladorRelatorio
from controle.controlador_revisao import ControladorRevisao 


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        #self.__controlador_veiculo = ControladorVeiculo(self)
        #self.__controlador_revisao = ControladorRevisao(self)
        self.__controlador_cliente = ControladorCliente(self)

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        
        lista_opcoes = {1: self.iniciar_veiculo, 2: self.iniciar_revisao, 3: self.abrir_controlador_cliente, 0: self.encerra_sistema}

        while True:

            opcao_escolhida = self.__tela_sistema.tela_opcoes()

            funcao_escolhida = lista_opcoes[opcao_escolhida]

            funcao_escolhida()

    def abrir_controlador_cliente(self):
        self.__controlador_cliente.abre_tela()

    def iniciar_revisao(self):
        # Chama o controlador de Revisao
        self.__controlador_revisao.abre_tela() 

    def iniciar_veiculo(self):
        # Chama o controlador de Veiculo
        self.__controlador_veiculo.abre_tela()

    def encerra_sistema(self):
        exit(0)
