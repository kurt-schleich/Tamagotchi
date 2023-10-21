class Tamagotchi:

    def __init__(self, energiaMax:int, saciedadeMax:int, limpezaMax:int, idadeMax:int ):
        self.saciedade_Max = saciedadeMax
        self.saciedade = saciedadeMax
        self.energia_Max = energiaMax
        self.energia = energiaMax
        self.limpeza_Max = limpezaMax
        self.limpeza = limpezaMax
        self.idade = 0
        self.idade_Max = idadeMax
        self.diamantes = 0
        self.vida = True

    def getEnergiaMax(self):
        return self.energia_Max

    def getSaciedadeMax(self):
        return self.saciedade_Max

    def getLimpezaMax(self):
        return self.limpeza_Max

    def getIdadeMax(self):
        return self.idade_Max

    def getEnergiaAtual(self):
        return self.energia

    def getSaciedadeAtual(self):
        return self.saciedade

    def getLimpezaAtual(self):
        return self.limpeza

    def getIdadeAtual(self):
        return self.idade

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        return self.vida

    def brincar(self):
        if self.vida:
            self.energia = self.energia - 2
            self.saciedade = self.saciedade - 1
            self.limpeza = self.limpeza - 3
            self.idade += 1
            self.diamantes += 1
            if self.energia_Max < self.energia:
                self.energia = self.energia_Max
            if self.saciedade_Max < self.saciedade:
                self.saciedade = self.saciedade_Max
            if self.limpeza_Max < self.limpeza:
                self.limpeza = self.limpeza_Max
            if self.energia <= 0:
                self.vida = False
                self.energia = 0
            if self.saciedade <= 0:
                self.vida = False
                self.saciedade = 0
            if self.limpeza <= 0:
                self.vida = False
                self.limpeza = 0
            elif self.idade >= self.idade_Max:
                self.vida = False
                self.idade = self.idade_Max
            return True
        else:
            return False

    def comer(self):
        if self.vida:
            self.energia = self.energia - 1
            self.saciedade = self.saciedade + 4
            self.limpeza = self.limpeza - 2
            self.idade += 1
            if self.energia_Max < self.energia:
                self.energia = self.energia_Max
            if self.saciedade_Max < self.saciedade:
                self.saciedade = self.saciedade_Max
            if self.limpeza_Max < self.limpeza:
                self.limpeza = self.limpeza_Max
            if self.energia <= 0:
                self.vida = False
                self.energia = 0
            if self.saciedade <= 0:
                self.vida = False
                self.saciedade = 0
            if self.limpeza <= 0:
                self.vida = False
                self.limpeza = 0
            if self.idade >= self.idade_Max:
                self.vida = False
                self.idade = self.idade_Max
            return True
        else:
            return False

    def dormir(self):
        if self.energia <= self.energia_Max - 5:
            if self.vida:
                self.saciedade = self.saciedade - 2
                for i in range(self.energia_Max-self.energia):
                    self.energia = self.energia + 1
                    self.idade = self.idade + 1
                    if self.energia_Max < self.energia:
                      self.energia = self.energia_Max
                    if self.saciedade_Max < self.saciedade:
                        self.saciedade = self.saciedade_Max
                    if self.limpeza_Max < self.limpeza:
                        self.limpeza = self.limpeza_Max
                    if self.energia <= 0:
                        self.vida = False
                        self.energia = 0
                    if self.saciedade <= 0:
                        self.vida = False
                        self.saciedade = 0
                    if self.limpeza <= 0:
                        self.vida = False
                        self.limpeza = 0
                    if self.idade > self.idade_Max:
                        self.vida = False
                        self.idade = self.idade_Max

                return True
            else:
                return False
        else:
            return False

    def banhar(self):
        if self.vida:
            self.limpeza = self.limpeza_Max
            self.energia = self.energia - 3
            self.saciedade = self.saciedade - 1
            self.idade += 2
            if self.energia_Max < self.energia:
                self.energia = self.energia_Max
            if self.saciedade_Max < self.saciedade:
                self.saciedade = self.saciedade_Max
            if self.limpeza_Max < self.limpeza:
                self.limpeza = self.limpeza_Max
            if self.energia <= 0:
                self.vida = False
                self.energia = 0
            if self.saciedade <= 0:
                self.vida = False
                self.saciedade = 0
            if self.limpeza <= 0:
                self.vida = False
                self.limpeza = 0
            if self.idade >= self.idade_Max:
                self.vida = False
                self.idade = self.idade_Max
            return True
        else:
            return False
