from limite.tela_sistema import TelaSistema
from controle.controlador_veiculo import ControladorVeiculo
from controle.controlador_cliente import ControladorCliente
from controle.controlador_relatorio import ControladorRelatorio
from controle.controlador_revisao import ControladorRevisao 



class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        
        print("INICIALIZANDO SISTEMA")
        
        self.abre_tela()

    def controlador_veiculos(self):
        print (">> CONTROLADOR DE VEICULOS SELECIONADO")
    
    def abre_tela(self):
        print(">>Abrindo tela")
        lista_opcoes = {1: self.controlador_veiculos}

        while True:

            opcao_escolhida =       self.__tela_sistema.tela_opcoes()

            servico_escolhido = lista_opcoes[opcao_escolhida]

            servico_escolhido()