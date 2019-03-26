class ENDERECO:
    """Exceções:
                Apenas COMPLEMENTO pode ser vazio.
                CEP: Não negativo, não ter mais nem menos q 8 digitos.
                NUMERO: não pode ser negativo.
                """

    def __init__(self, Rua, Num, Comp, Bair, CEP, Cid, Est):
        self._logradouro = Rua
        self._numero = Num
        self._complemento = Comp
        self._bairro = Bair
        self._cep = CEP
        self._cidade = Cid
        self._estado = Est

    def setRua(self, Rua):
        self._logradouro = Rua
    def getRua(self):
        return self.__logradouro

    def setNum(self, Num):
        self._numero = Num
    def getNum(self):
        return self.__numero

    def setComplemento(self, Comp):
        self.__complemento = Comp
    def getComplemento(self):
        return self.__complemento

    def setBairro(self, Bair):
        self.__bairro = Bair
    def getBairro(self):
        return self.__bairro

    def setCEP(self, CEP):
        self.__cep = CEP
    def getCEP(self):
        return self.__cep

    def setCidade(self, Cid):
        self.__cidade = Cid
    def getCidade(self):
        return self.__cidade

    def setEstado(self, Est):
        self.__estado = Est
    def getEstado(self):
        return self.__estado

class ENDERECOE:
    """Exceções:
                Apenas COMPLEMENTO pode ser vazio.
                CEP: Não negativo, não ter mais nem menos q 8 digitos.
                NUMERO: não pode ser negativo.
                """

    def __init__(self, RuaE, NumE, CompE, BairE, CEPE, CidE, EstE):
        self._logradouroE = RuaE
        self._numeroE = NumE
        self._complementoE = CompE
        self._bairroE = BairE
        self._cepE = CEPE
        self._cidadeE = CidE
        self._estadoE= EstE

    def setRuaE(self, RuaE):
        self._logradouroE = RuaE
    def getRuaE(self):
        return self.__logradouroE

    def setNumE(self, NumE):
        self._numeroE = NumE
    def getNumE(self):
        return self.__numeroE

    def setComplementoE(self, CompE):
        self.__complementoE = CompE
    def getComplementoE(self):
        return self.__complementoE

    def setBairroE(self, BairE):
        self.__bairroE = BairE
    def getBairroE(self):
        return self.__bairroE

    def setCEPE(self, CEPE):
        self.__cepE = CEPE
    def getCEPE(self):
        return self.__cepE

    def setCidadeE(self, CidE):
        self.__cidadeE = CidE
    def getCidadeE(self):
        return self.__cidadeE

    def setEstadoE(self, EstE):
        self.__estadoE = EstE
    def getEstadoE(self):
        return self.__estadoE
