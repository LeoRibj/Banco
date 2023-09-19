from contas import Conta
class Basedados:
    
    def __init__(self)->None:
        self.__contas=[]
    
    def addcontas(self,conta:Conta)->None:
        self.__contas.append(conta)
    
    def encontrar(self,numeroc:int=-1)->Conta:
         if numeroc>0 and isinstance(numeroc,int):
              conta=list(filter(lambda conta:conta.getnum()==numeroc,self.__contas))
              if len((conta))>0:
                   return conta[0]
              return None
         return None #type: ignore




