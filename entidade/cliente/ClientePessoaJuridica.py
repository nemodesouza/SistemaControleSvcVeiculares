from cliente.abstractCliente import AbstractCliente
from entidade.veiculo import Veiculo
 
 class clientePessoaJuridica(AbstractCliente):
     
     def __init__(self, codigo: int, nome: str, telefone: int, endereco: str, data_fundacao: str, cnpj: str, veiculo:Veiculo):
         super().__init_(codigo, nome, telefone, endereco)
         self.__data_fundacao = data_fundacao
         self.__cnpj = cnpj
         self.__veiculo = veiculo

    @property
    def data_fundacao(self):
        return self.__data_fundacao

    @data_fundacao.setter
    def data_fundacao(self):
        if isinstance (data_fundacao, str):
            self.__data_fundacao = data_fundacao
            
    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self):
        if isinstance (cnpj, str):
            self.cnpj = cnpj

    @property
    def veiculo(Veiculo): #confirmar se é isto mesmo
        return self.__veiculo
 
    @veiculo.setter
    def veiculo(Veiculo): #confirmar se é isso mesmo
        if isinstance(veiculo, entidade.veiculo.Veiculo):
            self.__veiculo = veiculo


 