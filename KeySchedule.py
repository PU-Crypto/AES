#KeySchedule
import SubBytes
from Tables import RijndaelRcon
import math

def RotWord(Spalte):
    #Verschiebe die Plaetze im Array
    output = list()
    output[0]=Spalte[1]
    output[1]=Spalte[2]
    output[2]=Spalte[3]
    output[3]=Spalte[0]

    return output

def XorRcon(Spalte, SpalteVor4, RconCount):
	#Verknepfe Schriit fuer Schritt die Sonderfaelle Xor, inklusive der RconTabelle
	output = list()
	for i in range(0,4):
		output[i] = hex(int(Spalte[i], 16)^int(SpalteVor4[i], 16)^int(RijndaelRcon.Rcon[RconCount], 16))

	return output

def Xor(Spalte, SpalteVor4):
	#Verknuepfe Wert fuer Wert Xor
	output = list()
	for i in range(0,4):
		output[i] = hex(int(Spalte[i], 16)^int(SpalteVor4[i], 16))#Hexadezimal

	return output



def KeySchedule(Cipher):
	#Erweitere den Schluessel
    for i in range(4,40,4):
      	roundCounter = 0
        Cipher[i] = RotWord(Cipher[i-1]])
        Cipher[i] = SubBytes.TranslateToSBox(Cipher[i-1])
        Cipher[i] = XorRcon(Cipher[i],Cipher[i-4]],roundCounter)
        roundCounter++
        for j in range(i,i+4):
        	Cipher[j] = Xor(Chipher[j-1],Chipher[j-4])

