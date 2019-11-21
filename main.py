#!/usr/bin/python3.6

import add
import control
import datamemory
import alu
import end
import Mux
import registers
import shift_left_2
import Sign_Extend
import re

def register_1(result, Registers): #como melhorar isso?
    if (result == 't0'):
        Registers.setRead_register_1(8)
    elif (result == 't1'):
        Registers.setRead_register_1(9)
    elif (result == 't2'):
        Registers.setRead_register_1(10)
    elif (result == 't3'):
        Registers.setRead_register_1(11)
    elif (result == 't4'):
        Registers.setRead_register_1(12)
    elif (result == 't5'):
        Registers.setRead_register_1(13)
    elif (result == 't6'):
        Registers.setRead_register_1(14)
    elif (result == 't7'):
        Registers.setRead_register_1(15)
    elif (result == 's0'):
        Registers.setRead_register_1(16)
    elif (result == 's1'):
        Registers.setRead_register_1(17)
    elif (result == 's2'):
        Registers.setRead_register_1(18)
    elif (result == 's3'):
        Registers.setRead_register_1(19)
    elif (result == 's4'):
        Registers.setRead_register_1(20)
    elif (result == 's5'):
        Registers.setRead_register_1(21)
    elif (result == 's6'):
        Registers.setRead_register_1(22)
    elif (result == 's7'):
        Registers.setRead_register_1(23)
    elif (result == 't8'):
        Registers.setRead_register_1(24)
    elif (result == 't9'):
        Registers.setRead_register_1(25)
    elif (result == 'zero'):
        Registers.setRead_register_1(26)
    else:
        print('Registrador não existe')

def register_2(result, Registers):
    if (result == 't0'):
        Registers.setRead_register_2(8)
    elif (result == 't1'):
        Registers.setRead_register_2(9)
    elif (result == 't2'):
        Registers.setRead_register_2(10)
    elif (result == 't3'):
        Registers.setRead_register_2(11)
    elif (result == 't4'):
        Registers.setRead_register_2(12)
    elif (result == 't5'):
        Registers.setRead_register_2(13)
    elif (result == 't6'):
        Registers.setRead_register_2(14)
    elif (result == 't7'):
        Registers.setRead_register_2(15)
    elif (result == 's0'):
        Registers.setRead_register_2(16)
    elif (result == 's1'):
        Registers.setRead_register_2(17)
    elif (result == 's2'):
        Registers.setRead_register_2(18)
    elif (result == 's3'):
        Registers.setRead_register_2(19)
    elif (result == 's4'):
        Registers.setRead_register_2(20)
    elif (result == 's5'):
        Registers.setRead_register_2(21)
    elif (result == 's6'):
        Registers.setRead_register_2(22)
    elif (result == 's7'):
        Registers.setRead_register_2(23)
    elif (result == 't8'):
        Registers.setRead_register_2(24)
    elif (result == 't9'):
        Registers.setRead_register_2(25)
    elif (result == 'zero'):
        Registers.setRead_register_2(26)
    elif(result.isnumeric() == True):
        Registers.setAux(int(result))
    else:
        print('Registrador não existe')

def register_Witre(result, Registers):
        if (result == 't0'):
            Registers.setWitre_register(8)
        elif (result == 't1'):
            Registers.setWitre_register(9)
        elif (result == 't2'):
            Registers.setWitre_register(10)
        elif (result == 't3'):
            Registers.setWitre_register(11)
        elif (result == 't4'):
            Registers.setWitre_register(12)
        elif (result == 't5'):
            Registers.setWitre_register(13)
        elif (result == 't6'):
            Registers.setWitre_register(14)
        elif (result == 't7'):
            Registers.setWitre_register(15)
        elif (result == 's0'):
            Registers.setWitre_register(16)
        elif (result == 's1'):
            Registers.setWitre_register(17)
        elif (result == 's2'):
            Registers.setWitre_register(18)
        elif (result == 's3'):
            Registers.setWitre_register(19)
        elif (result == 's4'):
            Registers.setWitre_register(20)
        elif (result == 's5'):
            Registers.setWitre_register(21)
        elif (result == 's6'):
            Registers.setWitre_register(22)
        elif (result == 's7'):
            Registers.setWitre_register(23)
        elif (result == 't8'):
            Registers.setWitre_register(24)
        elif (result == 't9'):
            Registers.setWitre_register(25)
        elif (result == 'zero'):
            Registers.setWitre_register(26)
        else:
            print('Registrador não existe')


def main():
    arq = open('programa.asm', 'r')
    instrucao = arq.readlines()


    for linha in instrucao:
        linha = linha.replace('$', '')  # substituindo '$' por '' (nada)
        linha = linha.replace(',', '')  # substituindo ',' por '' (nada)
        linha = linha.strip()  # tirado espaços a direita e esquerda desnecessarios
        result = linha.split()  # separando cada palavra em uma lista
        print(result)

        Registers = registers.Registers()
        Control = control.Control()
        AL = alu.ALU()

        if (result[0] == 'ADD'):
            Control.setIntrucion('000000', '32')
            Control.control()

            if(Control.getRegWrite() == True):
                register_1(result[2], Registers)
                register_2(result[3], Registers)
                register_Witre(result[1], Registers)


            AL.setRd(Registers.getValor_write())
            AL.setRs(Registers.getValor_register_1())
            AL.setRt(Registers.getValor_register_2())
            result_op = AL.alu(Control.getALUOp())
            print(result_op)
            Registers.setWrite_data(result_op)




        elif(result[0] == 'ADDI'):
            Control.setIntrucion('001000', '8')
            Control.control()

            if (Control.getRegWrite() == True):
                register_1(result[2], Registers)
                register_2(result[3], Registers)
                register_Witre(result[1], Registers)
            AL.setRd(Registers.getValor_write())
            AL.setRt(Registers.getAux())
            result_op = AL.alu(Control.getALUOp())
            print(result_op)
            Registers.setWrite_data(result_op)
        elif(result[0] == 'SUB'):
            Control.setIntrucion('000000', '34')
            Control.control()

            if (Control.getRegWrite() == True):
                register_1(result[2], Registers)
                register_2(result[3], Registers)
                register_Witre(result[1], Registers)

            AL.setRd(Registers.getValor_write())
            AL.setRs(Registers.getValor_register_1())
            AL.setRt(Registers.getValor_register_2())
            result_op = AL.alu(Control.getALUOp())
            print(result_op)
            Registers.setWrite_data(result_op)
    arq.close()

if __name__ == '__main__':
    main()
