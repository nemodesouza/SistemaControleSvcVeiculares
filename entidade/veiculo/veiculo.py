class Veiculo:

    def __init__(self, modelo: str, placa: str, ano: int, quilometragem: int):
        self.__modelo = modelo
        self.__placa = placa 
        self.__ano = ano 
        self.__quilometragem = quilometragem 

    @property
    def modelo(self) -> str:
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo: str):
        if isinstance(modelo, str):
            self.__modelo = modelo 

    @property
    def placa(self) -> str:
        return self.__placa

    @placa.setter
    def placa(self, placa: int):
        if isinstance(placa, str):
            self.__placa = placa 

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        if isinstance(ano, int):
            self.__ano = ano 

    @property
    def quilometragem(self) -> int:
        return self.__quilometragem

    @quilometragem.setter
    def quilometragem(self, quilometragem: int):
        if isinstance(quilometragem, int):
            self.__quilometragem = quilometragem