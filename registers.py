class registers:
    RegWrite = False
    Read_register_1 = False
    Read_register_2 = False
    Write_register = False
    Write_data = []
    Read_data_1 = []
    Read_data_2 = []

    def setRegWrite(self, state):
        self.RegWrite = state

    def setRead_register_1(self, state):
        self.Read_register_1 = state

    def setRead_register_2(self, state):
        self.Read_register_2 = state

    def setWitre_register(self, state):
        self.Write_register = state

    def setWrite_data(self, state):
        self.Write_data = state

    def getRead_data_1(self):
        return self.Read_data_1

    def getRead_register_2(self):
        return self.Read_register_2

    def getWitre_register(self):
        return self.Write_register

    def setWrite_data(self):
        return self.Write_data
