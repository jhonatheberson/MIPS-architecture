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

s1 =0
arq = open('programa.asm', 'r')
instrucao = arq.readlines()

for linha in instrucao:
    linha =  linha.replace('$','') #substituindo '$' por '' (nada)
    linha =  linha.replace(',','') #substituindo ',' por '' (nada)
    linha = linha.strip() #tirado espaços a direita e esquerda desnecessarios
    result = linha.split() # separando cada palavra em uma lista
    print(result)

    if(result[0] == 'ADDI'):
        AL = alu.ALU
        AL.setOpcode(AL, 0)
        #print(AL.getOpcode(AL))
        AL.setFunct(AL,32)
        #print(AL.getFunct(AL))
        AL.setRd(AL, result[1])
        #print(AL.getRd(AL))
        AL.setRs(AL,0)
        #print(AL.getRs(AL))
        AL.setRt(AL, int(result[3]))
        #print(AL.getRt(AL))

        result[1] = AL.alu(AL)

        print(s1)
        print(result)



    elif(result[0] == 'ADD'):
        ALU = alu

    elif(result[0] == 'SUB'):
        ALU = alu
arq.close()