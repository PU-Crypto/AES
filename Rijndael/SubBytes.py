from Rijndael.Tables import RijndaelSBox


def TranslateToSBox(Spalte): #Erhalte einen eindimensionalen Array mit 4 Strings vom Format 0xab. ab Element aus {0,1...,f}
	
	Translated = list()
	for Wert in Spalte:
		#Wert = format(int(Wert), '02x') # Konvertiere die Hexadezimalzahl in einen String
		fd = Wert[-2] #Erste Stelle
		sd = Wert[-1] #Zweite Stelle
		
		fd = int(fd , 16)
		sd = int(sd , 16)

		output = RijndaelSBox.SBox[fd]
		Translated.append(format(output[sd],'#04x'))
	return Translated
	
def SubBytes(Block):
	#Hole eine Spalte aus dem Block
	for i in range(0,4,1):
		Block[i] = TranslateToSBox(Block[i])
	return Block
