class Registers:
    def __init__(self):
        self.RegWrite = False
        self.Read_register_1 = None
        self.Read_register_2 = None
        self.Write_register = None
        self.Write_data = None
        self.Read_data_1 = None
        self.Read_data_2 = None
        self.aux = None
        self.Register_bank = [0,0,0,0,0,0,0,3,4,5,6,32,22,43,54,33,43,29,30,10,20,32,324,323,43,102]

    def setAux(self, state):
        self.aux = state

    def setRegWrite(self, state):
        self.RegWrite = state

    def setRead_register_1(self, valor):
        self.Read_register_1 = valor

    def setRead_register_2(self, valor):
        self.Read_register_2 = valor

    def setWitre_register(self, valor):
        self.Write_register = valor

    def setWrite_data(self, state):
        self.Write_data = state

    def getRead_data_1(self):
        return self.Read_data_1

    def getRead_register_2(self):
        return self.Read_register_2

    def getRead_register_1(self):
        return self.Read_register_1

    def getWitre_register(self):
        return self.Write_register

    def getValor_register_2(self):
        return self.Register_bank[self.Read_register_2]

    def getValor_register_1(self):
        return self.Register_bank[self.Read_register_1]

    def getValor_write(self):
        return self.Register_bank[self.Write_register]

    def getAux(self):
        return int(self.aux)

    def getWrite_data(self):
        return self.Write_data
