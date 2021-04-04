from limite.tela_revisao import TelaRevisao
from entidade.revisao.revisao import Revisao 

class ControladorRevisao():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_revisao = TelaRevisao()
        

    def abre_tela(self):
        lista_opcoes = {1: self.iniciar_revisao, 2: self.voltar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_revisao.tela_opcoes()]()

    def iniciar_revisao(self): 
        self.__tela_revisao.listar_revisoes(Revisao.lista_substituicoes, Revisao.lista_verificacoes)
        
    def voltar(self):
        pass 

     