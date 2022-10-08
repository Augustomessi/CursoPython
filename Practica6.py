# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:30:12 2022

@author: DET PC
"""

def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=" ")
        """ c=a+b
        a=b
          b=c"""
        a,b=b,a+b # es otra manera de escribir las lineas 12,13,14
        print() # imprime un espacio
        
fib(8)