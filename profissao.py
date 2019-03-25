from empresa import *
class PROFISSAO(EMPRESA):
    def __init__(self, Func):
        EMPRESA.__init__(self, TelE)
        self.__funcao = Func

    def setFuncao(self, Func):
        self.__funcao = Func
    def getFuncao(self):
        return self.__funcao