 # -*- coding: utf-8 -*-
#KeySchedule
from Rijndael.SubBytes import *
from Rijndael.Tables import RijndaelRcon
import math

def RotWord(Spalte):
    #Verschiebe die Plaetze im Array
    output = list()
    output.append(Spalte[1])
    output.append(Spalte[2])
    output.append(Spalte[3])
    output.append(Spalte[0])
    return output

def XorRcon(Spalte, SpalteVor4, RconCount):
    #Verknuepfe Schritt fuer Schritt die Sonderfaelle(immer die erste Spalte eines RoundKeys) Xor, inklusive der RconTabelle
    output = list()
    Rcon = RijndaelRcon.Rcon[RconCount]
    for i in range(0,4):
        output.append(format(int(Spalte[i],16)^int(SpalteVor4[i], 16)^int(format(Rcon[i], '#04x'),16), '#04x'))

    return output

def Xor(Spalte, SpalteVor4):
    #Verknuepfe Wert fuer Wert Xor
    output = list()
    for i in range(0,4):
        output.append(format(int(Spalte[i], 16)^int(SpalteVor4[i], 16), '#04x'))#Hexadezimal

    return output



def KeySchedule(Key):
    #Erweitere den Schluessel auf insgesamt 10 weitere von einander abhaengige Schluessel
    roundCounter = 0
    for i in range(4,41,4):
        Key.append(RotWord(Key[i-1]))
        Key[i] = TranslateToSBox(Key[i])
        Key[i] = XorRcon(Key[i],Key[i-4],roundCounter)
        roundCounter += 1
        for j in range(i+1,i+4):
            Key.append(Xor(Key[j-1],Key[j-4]))
            
    return Key
