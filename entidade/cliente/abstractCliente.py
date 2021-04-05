

class AbstractCliente:
    
    
    def __init__ (self, codigo: int, nome: str, telefone: int, endereco: str):
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance (nome, str):
            self.__nome = nome
        if isinstance(telefone, int):
            self.__telefone = telefone
        if isinstance(endereco, str):
            self.__endereco = endereco
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo:int):
        if isinstance(codigo, int):
            self.__codigo
     
    @property		
    def nome(self) ->str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
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

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco
    
     