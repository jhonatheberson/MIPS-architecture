class PortAnd():
    input_1 = False
    input_2 = False
    output = False

    def portAnd(self):
        if self.input_1 == self.input_2 == true:
            self.output = True
        else:
            self.output = False

    def setInput_1(self, state):
        self.input_1 = state

    def setInput_2(self, state):
        self.input_2 = state

    def getAnd(self):
        return self.output

