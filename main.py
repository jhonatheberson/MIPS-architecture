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

global zero
zero = 0
global t0, t1, t2, t3, t4,t5, t6, t7
global s0, s1, s2, s3, s4, s5, s6, s7
global t8, t9

arq = open('programa.asm', 'r')
instrucao = arq.readlines()

for linha in instrucao:
    result = linha.split()

    if(result[0] == 'ADDI'):
        ALU = alu.ALU
        #ALU.setOpcode(alu, 0)
        #ALU.setFunct(alu,32)
        #ALU.setRd(alu, result[1])
        #ALU.setRs(alu,zero)
        #ALU.setRt(alu, int(result[3]))
        #ALU.alu(alu)
        print(result[1])
        print(result[2])
        print(result[3])
        result[1]:2


    elif(result[0] == 'ADD'):
        ALU = alu

    elif(result[0] == 'SUB'):
        ALU = alu
arq.close()