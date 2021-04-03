from cliente.abstractCliente import AbstractCliente
from entidade.veiculo import Veiculo
 
 class clientePessoaFisica(AbstractCliente):
     
     def __init__(self, codigo: int, nome: str, telefone: int, endereco: str, data_nascimento: str, cpf: str, rg: str, orgao_emissor: str, veiculo:Veiculo)

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self):
        if isinstance (data_nascimento, str):
            self.__data_nascimento = data_nascimento
            
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self):
        if isinstance (cpf, str):
            self.cpf = cpf

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self):
        if isinstance (rg, str):
            self.rg = rg

    @property
    def orgao_emissor(self):
        return self.__orgao_emissor
    
    @orgao_emissor.setter
        def orgao_emissor(self):
            if isinstance (orgao_emissor, str):
                self.__orgao_emissor = orgao_emissor

    @property
    def veiculo(Veiculo): #confirmar se é isto mesmo
        return self.__veiculo
 
    @veiculo.setter
    def veiculo(Veiculo): #confirmar se é isso mesmo
        if isinstance(veiculo, entidade.veiculo.Veiculo):
            self.__veiculo = veiculo


