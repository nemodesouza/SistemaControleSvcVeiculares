from limite.tela_sistema import TelaSistema
from controle.controlador_revisao import ControladorRevisao
from controle.controlador_veiculo import ControladorVeiculo 

class ControladorSistema():

<<<<<<< HEAD
class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        #self.__controlador_veiculo = ControladorVeiculo(self)
        #self.__controlador_revisao = ControladorRevisao(self)
        self.__controlador_cliente = ControladorCliente(self)
=======
    def __init__(self):
        self.__controlador_veiculo = ControladorVeiculo(self)
        self.__controlador_revisao = ControladorRevisao(self)
        self.tela_sistema = TelaSistema()
>>>>>>> origin/Nemo

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
<<<<<<< HEAD
        
        lista_opcoes = {1: self.iniciar_veiculo, 2: self.iniciar_revisao, 3: self.abrir_controlador_cliente, 0: self.encerra_sistema}

        while True:

            opcao_escolhida = self.__tela_sistema.tela_opcoes()
=======

        lista_opcoes = {1: self.iniciar_veiculo, 2: self.iniciar_revisao, 0: self.encerra_sistema}

        while True:

            opcao_escolhida = self.tela_sistema.tela_opcoes()
>>>>>>> origin/Nemo

            funcao_escolhida = lista_opcoes[opcao_escolhida]

            funcao_escolhida()
<<<<<<< HEAD

    def abrir_controlador_cliente(self):
        self.__controlador_cliente.abre_tela()
=======
>>>>>>> origin/Nemo

    def iniciar_revisao(self):
        # Chama o controlador de Revisao
        self.__controlador_revisao.abre_tela() 

    def iniciar_veiculo(self):
        # Chama o controlador de Veiculo
        self.__controlador_veiculo.abre_tela()

    def encerra_sistema(self):
<<<<<<< HEAD
        exit(0)
=======
        exit(0)
>>>>>>> origin/Nemo
