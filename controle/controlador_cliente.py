from limite.tela_cliente import TelaCliente
from entidade.cliente.abstractCliente import AbstractCliente
from entidade.cliente.ClientePessoaFisica import ClientePessoaFisica
from entidade.cliente.ClientePessoaJuridica import ClientePessoaJuridica


class ControladorCliente():

    def __init__(self, controlador_sistema):
        self.__clientes_pf = []
        self.__clientes_pj = []
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema
    
    def cadastrar_cliente(self):

        # Método para definir se vai cadastrar pessoa física ou jurídica

        lista_tipos_cliente = {1: self.cadastra_pessoa_fisica, 2: self.cadastra_pessoa_juridica, 0: self.voltar}

        continua_tela_cliente = True

        while continua_tela_cliente:
            lista_tipos_cliente[self.__tela_cliente.tipo_de_cliente()]()
    
    def cadastra_pessoa_fisica(self):

        # Método para fazer o cadastro de cliente pessoa física

        dados_cliente = self.__tela_cliente.coleta_dados_pessoa_fisica()
        
        cliente = ClientePessoaFisica(int(dados_cliente["codigo"]), dados_cliente["nome"], dados_cliente["telefone"], dados_cliente["endereco"], dados_cliente["data_nascimento"], dados_cliente["cpf"], dados_cliente["rg"], dados_cliente["orgao_emissor"], dados_cliente["veiculo"])

        self.__clientes_pf.append(cliente)

        self.abre_tela()



    def cadastra_pessoa_juridica(self):

        # Método para fazer o cadastro de cliente pessoa física

        dados_cliente = self.__tela_cliente.coleta_dados_pessoa_juridica()
        
        cliente = ClientePessoaJuridica(dados_cliente["codigo"], dados_cliente["nome"], dados_cliente["telefone"], dados_cliente["endereco"], dados_cliente["data_fundacao"], dados_cliente["cnpj"], dados_cliente["veiculo"])

        self.__clientes_pj.append(cliente)

        self.abre_tela()

    def remover_cliente(self):
        print (">>> Aqui as opções de REMOVER cliente")
    
    def editar_cliente(self):
        print (">>> Aqui as opções de EDITAR cliente")
    
    def listar_clientes(self):

        lista_tipos_cliente = {1: self.listar_clientes_pf, 2: self.listar_clientes_pj, 0: self.voltar_tela_cliente}

        continua_tela_cliente = True

        while continua_tela_cliente:
            lista_tipos_cliente[self.__tela_cliente.tipo_de_cliente()]()
 
    def listar_clientes_pf(self):

        for cliente in self.__clientes_pf:
            self.__tela_cliente.listar_clientes_pf({'codigo': cliente.codigo, "nome": cliente.nome, "telefone": cliente.telefone, "endereco": cliente.endereco, "data_nascimento": cliente.data_nascimento, "cpf": cliente.cpf, "rg": cliente.rg, "orgao_emissor": cliente.orgao_emissor, "veiculo": cliente.veiculo})
    
    def listar_clientes_pj(self):

        for cliente in self.__clientes_pj:
            self.__tela_cliente.listar_clientes_pj({"codigo": cliente.codigo, "nome": cliente.nome, "telefone": cliente.telefone, "endereco": cliente.endereco, "data_fundacao": cliente.data_fundacao, "cnpj": cliente.cnpj, "veiculo": cliente.veiculo})
    
    def pegar_cliente_pelo_nome(Cliente):
        print (">>> Aqui as opções de PEGAR cliente pelo nome")
        
    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_cliente, 2: self.remover_cliente,  3: self.editar_cliente, 4: self.listar_clientes, 5: self.pegar_cliente_pelo_nome, 0: self.voltar}

        continua = True
        while continua:
   
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()

    def voltar(self):
        self.__controlador_sistema.abre_tela()

    def voltar_tela_cliente(self):
        self.abre_tela()

