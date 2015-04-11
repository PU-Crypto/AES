import math
import Utility.UTF8_Convert as Utf8
def CBC_Encrypt(plain, key, initvektor): #Diese Funktion erwartet einen Plaintext, der Bereits mit Utf-8 Utility vorbereitet wurde und einen Key, der eine Zahl ist und ein Initialisierungsvektor, der Dual und 8 Stellen lang ist.
	if len(initvektor) != 8:
		exit()
	Block = list()
	Block.append(initvektor)
	for i in range(1, len(plain)+1):
		dump = "{0:b}".format(int(plain[i-1],2)^int(Block[i-1],2))
		if len(dump)< 8:
			dump = Utf8.Padding(dump, 8)
		Block.append(dump)
	return Block

def CBC_Decrypt(cipher): #Diese Funktion erwartet die aus Rijndael-Decrypt ausgegebene Liste mit Hex-Werten und gibt eine Liste binärer Werte zurück
	plain = list()
	initvektor = "{0:b}".format(int(cipher[0],16))
	for i in range(1,len(cipher)):
		dump = "{0:b}".format(int(cipher[i],16) ^ int(cipher[i-1],16))
		if len(dump)< 8:
			dump = Utf8.Padding(dump, 8)
		plain.append(dump)
	return plain


def GenRijndaelBlock(BinArray): #Generiere einen zweidimensionalen zeilenorientierten Array aus einem Array mit hintereinander stehenden Werten: {0,1} und Konvertiere sie zu 0x..
	#Erweitere BinArray ggf. auf eine  durch 16 teilbare Menge an Werten
	while len(BinArray)%16 != 0:
		BinArray.append('00000000')

	#Erstelle einen Array mit Zeilen von 4 Stellen und einer durch 4 teilbaren Laenge
	Zeilen = list()
	dump = list()
	for i in range(0,len(BinArray)):
		HexWert = format(int(BinArray[i],2),'#04x')
		dump.append(HexWert)
		if len(dump) == 4:
			Zeilen.append(dump)
			dump = list()
	return Zeilen


