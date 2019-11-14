class ALU():
    opcode = None
    Rs = None
    Rt = None
    Rd = None
    shamt = None
    funct = None

    def alu(self):
        if self.opcode == 0 & self.funct == 32:
            Rd = Rs + Rt
            return Rd
        elif self.opcode == 0 & self.funct == 34:
            Rd = Rs - Rt
            return Rd
        elif self.opcode == 8 & self.funct == 1:
            Rd = Rs + Rt
            return Rd
        elif (self.opcode == 4 & self.funct == 1): # tipo I == 1
            print('não sei o que "BEQ"')
        elif (self.opcode == 2 & self.funct == 2): # tipo J == 2
            print('nao sei o que "J"')
        elif (self.opcode == 35 & self.funct == 1):
            print('nao sei o que "J"')
        else:
            print('nao sei o que "J"')

    def setOpcode(self, opcode):
        self.opcode = opcode

    def setRs(self, Rs):
        self.Rs = Rs

    def setRt(self, Rt):
        self.Rt = Rt

    def setRd(self, Rd):
        self.Rd = Rd

    def setShamt(self, shamt):
        self.shamt = shamt

    def setFunct(self, funct):
        self.funct = funct

    def getOpcode(self):
        return self.opcode

    def setRs(self):
        return self.Rs

    def setRt(self):
        return self.Rt

    def setRd(self):
        return self.Rd

    def setShamt(self):
        return self.shamt

    def setFunct(self):
        return self.funct
