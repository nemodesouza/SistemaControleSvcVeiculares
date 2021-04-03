class Verificacao():

    def __init__(self, identificador: int, descricao: str):
        self.__identificador = identificador 
        self.__descricao = descricao

    @property
    def identificador(self) -> int:
        return self.__identificador

    @property
    def descricao(self) -> str:
        return self.__descricao 

I = Verificacao(1, "Verificar nível do óleo do motor")

II = Verificacao(2, "Verificar o filtro de óleo do motor")

III = Verificacao(3, "Verificar o filtro de combustível")

IV = Verificacao(4, "Verificar o anel de vedação do bujão do cárter do motor")

V = Verificacao(5, "Verificar a anilha do mecanismo do pneu de estepe")

VI = Verificacao(6, "Verificar as velas de ignição")

VII = Verificacao(7, "Verificar o filtro de ar do motor")

VII = Verificacao(8, "Verificar o fluido de freio")

IX = Verificacao(9, "Verificar a correia dentada")

X = Verificacao(10, "Verificar a correia auxiliar")

XI = Verificacao(11, "Verificar o líquido de arrefecimento")