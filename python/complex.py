from os import *
from sys import *
from collections import *
from math import *



class ComplexNumbers:
    
    #create your class here.
    def __init__(self,real,imaginary):
        self.R=real
        self.I=imaginary
    
    def plus(self,C2):
        self.R=self.R+C2.R
        self.I=self.I+C2.I
        self.printComplex()
    def multiply(self,C2):
        real=self.R*C2.R - (self.I*C2.I)
        imaginary=self.R*C2.I + (self.I*C2.R)
        self.R=real
        self.I=imaginary
        self.printComplex()
    def printComplex(self):
        if self.I < 0:
            print(str(self.R)+" - i"+str(-self.I))
        else:
            print(str(self.R)+" + i"+str(self.I))
    
    
    
    
    
    
#Driver's code goes here.
r1,c1=map(int,input().split())


Complex1=ComplexNumbers(r1,c1)

r2,c2=map(int, input().split())

Complex2=ComplexNumbers(r2,c2)

choice=int(input())
if choice==1:
    Complex1.plus(Complex2)

if choice==2:
    Complex1.multiply(Complex2)
    
    
    
    
    
    
    
    
    
    
