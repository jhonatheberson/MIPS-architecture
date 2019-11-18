class ALU():
    opcode = None
    Rs = None
    Rt = None
    Rd = None
    shamt = None
    funct = None

    def teste(self):
        print('teste')

    def alu(self):
        if (self.opcode == 0 and self.funct == 32):
            self.Rd = self.Rs + self.Rt
            return self.Rd
        elif (self.opcode == 0 and self.funct == 34):
            self.Rd = self.Rs - self.Rt
            return Rd
        elif (self.opcode == 8 and self.funct == 1):
            self.Rd = self.Rs + self.Rt
            return Rd
        elif (self.opcode == 4 and self.funct == 1): # tipo I == 1
            print('não sei o que "BEQ"')
        elif (self.opcode == 2 and self.funct == 2): # tipo J == 2
            print('nao sei o que "J"')
        elif (self.opcode == 35 and self.funct == 1):
            print('nao sei o que "J"')
        elif(self.opcode == 43 and self.funct == 1):
            print('nao sei o que "J"')

    def setOpcode(self, opcode_final):
        self.opcode = opcode_final

    def setRs(self, Rs_final):
        self.Rs = Rs_final

    def setRt(self, Rt_final):
        self.Rt = Rt_final

    def setRd(self, Rd_final):
        self.Rd = Rd_final

    def setShamt(self, shamt_final):
        self.shamt = shamt_final

    def setFunct(self, funct_final):
        self.funct = funct_final

    def getOpcode(self):
        return self.opcode

    def getRs(self):
        return self.Rs

    def getRt(self):
        return self.Rt

    def getRd(self):
        return self.Rd

    def getShamt(self):
        return self.shamt

    def getFunct(self):
        return self.funct
