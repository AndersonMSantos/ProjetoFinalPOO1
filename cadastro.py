from paciente import *
class CADASTRO(PACIENTE):

    def __init__(self, Rua, Num , Comp, Bair, CEP, Cid, Est, Nome, Nasc, Civi, RG, CPF, Gen, Tel, Sang, RH, Idade, Altura, Peso, IMC, SUS, Priori):
        PACIENTE.__init__(self, Rua, Num , Comp, Bair, CEP, Cid, Est, Nome, Nasc, Civi, RG, CPF, Gen, Tel, Sang, RH, Idade, Altura, Peso, IMC, SUS, Priori)

    def setNome(self, Nome):
        self.__Nome = input('Nome: ')
    def getNome(self):
        return self.__Nome

    input('Data de Nascimento: ')
    input('Estado Civil: ')
    input('RG: ')
    input('CPF: ')
    input('Genero: ')
    input('Telefone: ')
    input('Tipo Sanguineo: ')
    input('RH: ')