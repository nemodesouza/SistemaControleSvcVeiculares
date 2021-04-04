from entidade.veiculo.veiculo import Veiculo 
from entidade.revisao.substituicao import Substituicao
from entidade.revisao.verificacao import Verificacao

class Revisao():
    def __init__(self, verificacao: Verificacao, substituicao: Substituicao, veiculo: Veiculo):
        if isinstance(verificacao, Verificacao):
            self.__verificacao = verificacao
        if isinstance(substituicao, Substituicao):
            self.__substituicao = verificacao
        if isinstance(veiculo, Veiculo):
            self.__veiculo = veiculo

    @property
    def verificacao(self) -> Verificacao:
        return self.__verificacao

    @property
    def substituicao(self) -> Substituicao:
        return self.__substituicao

    @property
    def veiculo(self) -> Veiculo:
        return self.__veiculo

    I = Substituicao(1, "Substituir óleo do motor")

    II = Substituicao(2, "Substituir o filtro de óleo do motor")

    III = Substituicao(3, "Substituir o filtro de combustível")

    IV = Substituicao(4, "Substituir o anel de vedação do bujão do cárter do motor")

    V = Substituicao(5, "Substituir a anilha do mecanismo do pneu de estepe")

    lista_substituicoes = [I, II, III, IV, V]

    VI = Verificacao(6, "Verificar as velas de ignição")

    VII = Verificacao(7, "Verificar o filtro de ar do motor")

    VIII = Verificacao(8, "Verificar o fluido de freio")

    IX = Verificacao(9, "Verificar a correia dentada")

    X = Verificacao(10, "Verificar a correia auxiliar")

    XI = Verificacao(11, "Verificar o líquido de arrefecimento")

    lista_verificacoes = [VI, VII, VIII, IX, X]



    

  

    
