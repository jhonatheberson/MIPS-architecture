class Control():
    def __init__(self):
        self.intrucion = [None, None]
        self.RegDst = False
        self.Branch = False
        self.MemReadu = False
        self.MemtoReg = False
        self.ALUOp = None
        self.Memwrite = False
        self.ALUSrc = False
        self.RegWrite = False

    def control(self):
        if(self.intrucion[0] == '000000' and self.intrucion[1] == '32'):
            self.RegDst = True
            self.ALUOp = 0
            self.RegWrite = True
        elif(self.intrucion[0] == '000000' and self.intrucion[1] == '34'):
            self.RegDst = True
            self.ALUOp = 1
            self.RegWrite = True
        elif(self.intrucion[0] == '001000' and self.intrucion[1] == '8'):
            self.RegDst = True
            self.ALUOp = 2
            self.RegWrite = True

    def setIntrucion(self, strucion_final_0, strucion_final_1):#como melhorar isso?
        self.intrucion[0] = strucion_final_0
        self.intrucion[1] = strucion_final_1

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
        return self.intrucion

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