class Substituicao():

    def __init__(self, identificador: int, descricao: str):
        self.__identificador = identificador 
        self.__descricao = descricao

    @property
    def identificador(self):
        return self.__identificador

    @property
    def descricao(self):
        return self.__descricao 


I = Substituicao(1, "Substituir óleo do motor")

II = Substituicao(2, "Substituir o filtro de óleo do motor")

III = Substituicao(3, "Substituir o filtro de combustível")

IV = Substituicao(4, "Substituir o anel de vedação do bujão do cárter do motor")

V = Substituicao(5, "Substituir a anilha do mecanismo do pneu de estepe")

VI = Substituicao(6, "Substituir as velas de ignição")

VII = Substituicao(7, "Substituir o filtro de ar do motor")

VII = Substituicao(8, "Substituir o fluido de freio")

IX = Substituicao(9, "Substituir a correia dentada")

X = Substituicao(10, "Substituir a correia auxiliar")

XI = Substituicao(11, "Substituir o líquido de arrefecimento")