from limite.tela_sistema import TelaSistema
from controle.controlador_veiculo import ControladorVeiculo
from controle.controlador_cliente import ControladorCliente
from controle.controlador_relatorio import ControladorRelatorio
from controle.controlador_revisao import ControladorRevisao 



class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_cliente = ControladorCliente(self)

    def inicializa_sistema(self):

        self.abrir_tela()

    def abrir_controlador_cliente(self):
        self.__controlador_cliente.abrir_tela()

    def encerrar_sistema(self):
        try:
            1/0
        except:
            pass
        
        

    def controlador_veiculos(self):
        print (">> CONTROLADOR DE VEICULOS SELECIONADO -- EBA!!!")
    
    def abrir_tela(self):
        
        lista_opcoes = {1: self.controlador_veiculos, 2: self.abrir_controlador_cliente, 0: self.encerrar_sistema}

        continua = True

        try:
            while continua == True:

                opcao_escolhida =       self.__tela_sistema.tela_opcoes()

                servico_escolhido = lista_opcoes[opcao_escolhida]

                if servico_escolhido() != servico_escolhido(0):
                    servico_escolhido()

                else:
                    1/0
        except:
            pass
        