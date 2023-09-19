class Conta:
    def __init__(self,nome,saldo,numeroc)->None:
        self.__nome=nome
        self.__saldo=saldo
        self.__numeroc=numeroc
    def getnome(self)->str:
        return self.__nome
    def getnum(self)->int:
        return self.__numeroc
    def getsald(self)->float:
        return self.__saldo
    def somar(self,valor)->float:
        self.__saldo+=valor
        return valor
    def sub(self,valor)->float:
        self.__saldo-=valor
        return valor
    def tostring(self):
        return f'o nome cadastrado é {self.__nome} numero da conta {self.__numeroc} e o saldo de {self.__saldo} reais'
    