from limite.tela_cliente import TelaCliente
from entidade.cliente.abstractCliente import AbstractCliente
from entidade.cliente.ClientePessoaFisica import ClientePessoaFisica
from entidade.cliente.ClientePessoaJuridica import ClientePessoaJuridica


class ControladorCliente():

    def __init__(self, controlador_sistema):
        self.__clientes = []
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema
    
    def cadastrar_cliente(self):
        print (">>> Aqui as opções de CADASTRAR cliente")
    
    def remover_cliente(self):
        print (">>> Aqui as opções de REMOVER cliente")
    
    def editar_cliente(self):
        print (">>> Aqui as opções de EDITAR cliente")
    
    def listar_clientes(self):
        print (">>> Aqui as opções de LISTAR cliente")
    
    def pegar_cliente_pelo_nome(Cliente):
        print (">>> Aqui as opções de PEGAR cliente pelo nome")

    def abrir_tela(self):
        lista_opcoes = {1: self.cadastrar_cliente, 2: self.remover_cliente,  3: self.editar_cliente, 4: self.listar_clientes, 5: self.pegar_cliente_pelo_nome}

        continua = True
        while continua:
   
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()


