# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:11:19 2015

@author: Babbel
"""
def AddRoundKey(Key = [], Pretext = []):
    text = XOR(Pretext)    
    for i in range(0,4):
        text1 = text[i]
        key1 = Key[i]
        for j in range(0,4):
                print(text1[j])
                print(hex(key1[j]))                
                text1[j] = hex(int(text1[j],16)^int(hex(key1[j]),16))
        text[i] = text1
    for q in range(0,4):
        u = text[q]
        for p in range(0,4):
            y = u[j]            
            if len(y) < 4:
                a,b = y.split('x')
                y = str(a + 'x' + str(0) + b)
                u[j] = y
    return text 
    