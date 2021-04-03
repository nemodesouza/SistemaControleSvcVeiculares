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
		pass

    @property		
	def nome(self) ->str:
		pass
    
    @property
    def telefone(self) ->str:
		pass
    
    @property
    def endereco(self) ->str:
        pass

    @abstractmethod
     