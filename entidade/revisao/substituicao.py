class Substituicao():

    def __init__(self, identificador: int, descricao: str):
        self.__identificador = identificador 
        self.__descricao = descricao

    @property
    def identificador(self) -> int:
        return self.__identificador

    @property
    def descricao(self) -> str:
        return self.__descricao 