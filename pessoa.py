from endereco import *
class PESSOA(ENDERECO):

    def __init__(self, Rua, Num , Comp, Bair, CEP, Cid, Est, Nome, Nasc, Civi, RG, CPF, Gen, Tel, Sang, RH):
        ENDERECO.__init__(self, Rua, Num , Comp, Bair, CEP, Cid, Est)
        self.__nome = Nome #!= VAZIO
        self.__dataNas = Nasc #dataNas: !< 1900, !> 12 meses, !> 31 dias, NÃO dias, mês ou ano negativo, não pode ser 0/0/0,
        self.__estCiv = Civi #!= VAZIO
        self.__rg = RG #= 10 DIGITOS. NÃO NEGATIVO. DIFERENTE DE 00.000.000-00.
        self.__cpf = CPF #= 11 DIGITOS. //.             //.
        self.__genero = Gen #!= M/F. NÃO VAZIO
        self.__telefone = Tel #NÃO 0000-0000. NÃO NEGATIVO.
        self.__sangue = Sang #NÃO VAZIO (A, B, AB, O)
        self.__rh = RH #NÃO VAZIO (+, -)

    def setNome(self, Nome):
        self.__nome = Nome
    def getNome(self):
        return self.__nome

    def setNascimento(self, Nasc):
        self.__dataNas = Nasc
    def getNascimento(self):
        return self.__dataNas

    def setEstadoCivil(self, Civil):
        self.__estCiv = Civil
    def getEstadoCivil(self):
        return self.__estCiv

    def setRG(self, RG):
        self.__rg = RG
    def getRG(self):
        return self.__rg

    def setCPF(self, CPF):
        self.__cpf = CPF
    def get(self):
        return self.__cpf

    def setGenero(self, Gen):
        self.__genero = Gen
    def get(self):
        return self.__genero

    def setTelefone(self, Tel):
        self.__telefone = Tel
    def getTelefone(self):
        return self.__telefone

    def setTipoSangue(self, sang):
        self.__sangue = sang
    def getTipoSangue(self):
        return self.__sangue

    def setRH(self, RH):
        self.__rh = RH
    def getRH(self):
        return self.__rh