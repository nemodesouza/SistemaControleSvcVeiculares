from limite.tela_cliente import TelaCliente
from entidade.cliente.abstractCliente import AbstractCliente
from entidade.cliente.ClientePessoaFisica import ClientePessoaFisica
from entidade.cliente.ClientePessoaJuridica import ClientePessoaJuridica


class ControladorCliente():

    def __init__(self, controlador_sistema):
        self.__clientes = []
        self.___tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema
    
    def abre_tela():
        print (">> tela aberta de cliente")






