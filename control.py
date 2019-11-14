class control():
    intrucion = []
    RegDst = []
    Branch = []
    MemReadu = False
    MemtoReg = False
    ALUOp = False
    Memwrite = False
    ALUSrc = False
    RegWrite = False

    def setIntrucion(self, strucion_final):
        self.intrucion = strucion_final

    def setRegDst(self, RegDst_final):
        self.RegDst = RegDst_final

    def setBranch(self, Branch_final):
        self.Branch = Branch_final

    def setMemReadu(self, state):
        self.MemReadu = state

    def setMemtoReg(self, state):
        self.MemtoReg = state

    def setALUOp(self, state):
        self.ALUOp = state

    def setMemwrite(self,state):
        self.Memwrite = state

    def setRegWrite(self, state):
        self.RegWrite = state

    def setALUSrc(self, state):
        self.ALUSrc = state

    def getIntrucion(self):
        return self.strucion

    def getRegDst(self):
        return self.RegDst

    def getBranch(self):
        return self.Branch

    def getMemReadu(self):
        return self.MemReadu

    def getMemtoReg(self):
        return self.MemtoReg

    def getALUOp(self):
        return self.ALUOp

    def getMemwrite(self):
        return self.Memwrite

    def getRegWrite(self):
        return self.RegWrite

    def getALUSrc(self):
        return self.ALUSrc