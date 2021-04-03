from verificacao import Verificacao 
from substituicao import Substituicao
from veiculo import Veiculo 

class Revisao():
  def __init__(self, verificacao: Verificacao, substituicao: Substituicao, veiculo: Veiculo):
    self.__verificacao = []
    self.__substituicao = []
    self.__veiculo = Veiculo 

    
