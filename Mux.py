class Mux ():
    input_1 = 0
    input_2 = 1
    output = []  

    def mux ( self, input_1,input_2, output):
        if ( output == 0):
            return input_1
        else:
            return input_2
        
