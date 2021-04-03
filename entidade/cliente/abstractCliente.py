from abc import ABC, abstractmethod


class AbstractCliente (ABC):
    @property
	def __init__(self):
        pass
    
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
    