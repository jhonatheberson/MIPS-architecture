class Mux ():
    input_1 = []
    input_2 = []
    output = None

    def mux ( self, input_1,input_2, output):
        if (output == False):
            return input_1
        else:
            return input_2
        
