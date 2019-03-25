class ENDERECO:

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
        return self.Rua

    def setNum(self, Num):
        self._numero = Num
    def getNum(self):
        return self.Num

    def setComplemento(self, Comp):
        self.__complemento = Comp
    def getComplemento(self):
        return self.Comp

    def setBairro(self, Bair):
        self.__bairro = Bair
    def getBairro(self):
        return self.Bair

    def setCEP(self, CEP):
        self.__cep = CEP
    def getCEP(self):
        return self.CEP

    def setCidade(self, Cid):
        self.__cidade = Cid
    def getCidade(self):
        return self.Cid

    def setEstado(self, Est):
        self.__estado = Est
    def getEstado(self):
        return self.Est
