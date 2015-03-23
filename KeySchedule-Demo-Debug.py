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
        output.append(hex(int(Spalte[i],16)^int(SpalteVor4[i], 16)^int(format(Rcon[i], '#04x'),16)))

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
        print("RoundC: " + str(roundCounter) + " i: " + str(i) )
        print(Cipher[i-1])
        Cipher.append(RotWord(Cipher[i-1]))
        print("Rot " + str(Cipher[i]))
        Cipher[i] = SubBytes.TranslateToSBox(Cipher[i])
        print("SBox " + str(Cipher[i]))
        Cipher[i] = XorRcon(Cipher[i],Cipher[i-4],roundCounter)
        print("XorRcon" + str(Cipher[i]))
        roundCounter += 1
        for j in range(i+1,i+4):
            Cipher.append(Xor(Cipher[j-1],Cipher[j-4]))
            print("j: " + str(j) + " Chipher " + str(Cipher[j]))
    return Cipher

Key = list()
Key.append([0x2b, 0x7e, 0x15, 0x16])
Key.append([0x28, 0xae, 0xd2, 0xa6])
Key.append([0xab, 0xf7, 0x15, 0x88])
Key.append([0x09, 0xcf, 0x4f, 0x3c])

for Spalte in Key:
    for i in range(0,4):
        Spalte[i] = format(Spalte[i], '#04x')


ExpandedKey = KeySchedule(Key)
i=0
for Spalte in ExpandedKey:
    print(str(i) + " " + str(Spalte))
    if((i%4)==0):
        print()
    i+=1