import math
import UTF8_Convert as Utf8
def CBC_Encrypt(plain, key, initvektor): #Diese Funktion erwartet einen Plaintext, der Bereits mit Utf-8 Utility vorbereitet wurde und einen Key, der eine Zahl ist und ein Initialisierungsvektor, der Dual und 8 Steelen lang ist.
	if len(initvektor) < 8:
		exit()
	Block = list()
	Block.append(initvektor)
	for i in range(1, len(plain)):
		dump = "{0:b}".format(int(plain[i-1],2)^int(Block[i-1],2))
		if len(dump)< 8:
			dump = Utf8.Padding(dump, 8)
		Block.append(dump)
	return Block

def GenRijndaelBlock(BinArray): #Generiere einen Zweidimensionalen zeilenorientierten Array aus einem Array mit hintereinander stehenden Werten: {0,1} und Konvertiere sie zu 0x..
	RijndaelBlock = list()
	#Erweitere BinArray ggf. auf eine  durch 16 teilbare Menge an Werten
	while len(BinArray)%16 != 0:
		BinArray.append('00000000')

	#Erstelle einen Array mit Zeilen von 4 Stellen und einer durch 4 teilbaren Laenge
	Zeilen = list()
	zeilencount = 0
	dump = list()
	for i in range(0,len(BinArray)):
		HexWert = format(int(BinArray[i],2),'#04x')
		dump.append(HexWert)
		if len(dump) == 4:
			Zeilen.append(dump)
			dump = list()
	return Zeilen


plain = Utf8.UTFConvert('Ich mag Käse')
cipher = CBC_Encrypt(plain, bin(12345678), '10101011')
print(cipher)

RijndaelBlock = GenRijndaelBlock(cipher)


Block4x4 = list()
for i in range(0,len(RijndaelBlock)):
	Block4x4.append(RijndaelBlock[i])
	if len(Block4x4) == 4:

		#Call Rijndael here
		
		Block4x4 = list()