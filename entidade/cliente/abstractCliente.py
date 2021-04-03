from abc import ABC, abstractmethod


class AbstractCliente (ABC):
    @abstractmethod
	def __init__(self, codigo: int, nome: str, telefone: int, endereco: str):
        if isinstance (codigo, int):
            self.__codigo = codigo
        if isinstance (nome, str):
            self.__nome = mome
        if isinstance (telefone, int):
            self.__telefone = telefone
        if isinstance (endereco, str):
            self.__endereco = endereco
    
    @property
    def codigo(self) -> int:
		return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo:int):
        
        #gera número aleatório de código
        #verifica se número já existe
        #ver jeito de fazer um sequencial, pra economizar memória

        pass
    
    @property		
	def nome(self) ->str:
		return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        is instance (nome, str):
        self.__nome

    @property
    def telefone(self) ->str:
		return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance (telefone, str):
            self.__telefone

    @property
    def endereco(self) ->str:
        return self.__endereco

    @enderecos.setter
    def enderecos(self, enderecos: str):
        if isinstance(enderecos, str):
            self.__enderecos
    
     