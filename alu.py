class ALU():
    def __init__(self):
        self.Rs = None
        self.Rt = None
        self.Rd = None

    def alu(self, opcode):
        if  (opcode == 0):
            self.Rd = self.Rs + self.Rt
            return self.Rd
        elif (opcode == 1):
            self.Rd = self.Rs - self.Rt
            return self.Rd
        elif (opcode == 2):
            self.Rd = int(0) + self.Rt
            return self.Rd
        elif (opcode == 3): # tipo I == 1
            print('não sei o que "BEQ"')
        elif (opcode == 4): # tipo J == 2
            print('nao sei o que "J"')
        elif (opcode == 5 ):
            print('nao sei o que "J"')
        elif(opcode == 6):
            print('nao sei o que "J"')


    def setRs(self, Rs_final):
        self.Rs = Rs_final

    def setRt(self, Rt_final):
        self.Rt = Rt_final

    def setRd(self, Rd_final):
        self.Rd = Rd_final

    def getRs(self):
        return self.Rs

    def getRt(self):
        return self.Rt

    def getRd(self):
        return self.Rd


