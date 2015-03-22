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
		output.append(hex(Spalte[i]^SpalteVor4[i]^Rcon[i]))

	return output

def Xor(Spalte, SpalteVor4):
	#Verknuepfe Wert fuer Wert Xor
	output = list()
	for i in range(0,4):
		print(type(Spalte[i]))
		output.append(hex(int(str(Spalte[i]), 16)^int(str(SpalteVor4[i]), 16)))#Hexadezimal

	return output



def KeySchedule(Cipher):
	#Erweitere den Schluessel
    for i in range(4,41,4):
        roundCounter = 0
        Cipher.append(RotWord(Cipher[i-1]))
        Cipher[i] = SubBytes.TranslateToSBox(Cipher[i])
        Cipher[i] = XorRcon(Cipher[i],Cipher[i-4],roundCounter)
        roundCounter += 1
        for j in range(i,i+4):
        	Cipher[j] = Xor(Cipher[j-1],Cipher[j-4])
    return Cipher

Key = list()
Key.append([0x2b, 0x7e, 0x15, 0x16])
Key.append([0x28, 0xae, 0xd2, 0xa6])
Key.append([0xab, 0xf7, 0x15, 0x88])
Key.append([0x09, 0xcf, 0x4f, 0x3c])

ExpandedKey = KeySchedule(Key)