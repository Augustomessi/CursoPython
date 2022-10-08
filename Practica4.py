# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:11:45 2022

@author: DET PC
"""

while True:
    x=input("Ingrese un numero ")
    if x=='q' or x=='quit' :
        break
    
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
    