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

        lista_tipos_cliente = {1: self.cadastra_pessoa_fisica, 2: self.cadastra_pessoa_juridica}

        continua_tela_cliente = True

        while continua_tela_cliente:
            lista_tipos_cliente[self.__tela_cliente.tipo_de_cliente()]()
    
    def cadastra_pessoa_fisica(self):
        dados_cliente = self.__tela_cliente.coleta_dados_pessoa_fisica()
        
        print(">>>>> voltando da tela>>>>>")
        
        cliente = ClientePessoaFisica(dados_cliente["codigo"], dados_cliente["nome"], dados_cliente["telefone"], dados_cliente["endereco"], dados_cliente["data_nascimento"], dados_cliente["cpf"], dados_cliente["rg"], dados_cliente["orgao_emissor"], dados_cliente["veiculo"])

        print(">>>>> objeto cliente criado>>>>>")
        print(cliente.nome)

        self.__clientes.append(cliente)

        print(">>>>> append feito>>>>>")

        self.abre_tela()

        print(">>>>> tela>>>>>")

    def cadastra_pessoa_juridica(self):
        print (">>> CADASTRAR CLIENTE PESSOA JURÍDICA")

    def remover_cliente(self):
        print (">>> Aqui as opções de REMOVER cliente")
    
    def editar_cliente(self):
        print (">>> Aqui as opções de EDITAR cliente")
    
    def listar_clientes(self):
 
        for cliente in self.__clientes:
            self.__tela_cliente.listar_clientes({"codigo": cliente.codigo, "nome": cliente.nome, "telefone": cliente.telefone, "endereco": cliente.endereco, "data_nascimento": cliente.data_nascimento, "cpf": cliente.cpf, "rg": cliente.rg, "orgao_emissor": cliente.orgao_emissor, "veiculo": cliente.veiculo})
            
    
    def pegar_cliente_pelo_nome(Cliente):
        print (">>> Aqui as opções de PEGAR cliente pelo nome")
        
    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_cliente, 2: self.remover_cliente,  3: self.editar_cliente, 4: self.listar_clientes, 5: self.pegar_cliente_pelo_nome, 0: self.voltar}

        continua = True
        while continua:
   
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()

    def voltar(self):
        self.__controlador_sistema.abre_tela()


