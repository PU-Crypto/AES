#KeySchedule
import SubBytes
from Tables import RijndaelRcon
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
    #Verknepfe Schriit fuer Schritt die Sonderfaelle Xor, inklusive der RconTabelle
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



def KeySchedule(Cipher):
    #Erweitere den Schluessel
    roundCounter = 0
    for i in range(4,41,4):
        Cipher.append(RotWord(Cipher[i-1]))
        Cipher[i] = SubBytes.TranslateToSBox(Cipher[i])
        Cipher[i] = XorRcon(Cipher[i],Cipher[i-4],roundCounter)
        roundCounter += 1
        for j in range(i+1,i+4):
            Cipher.append(Xor(Cipher[j-1],Cipher[j-4]))
            
    return Cipher