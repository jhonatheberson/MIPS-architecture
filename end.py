class PortAnd():
    input_1 = false
    input_2 = false
    output = false

    def portAnd(self):
        if self.input_1 == self.input_2 == true:
            return true
        else:
            return false

    def setInput_1(self, state):
        self.input_1 = state

    def setInput_2(self, state):
        self.input_2 = state

    def getAnd(self):
        return = self.output

