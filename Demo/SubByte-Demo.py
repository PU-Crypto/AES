from Tables import RijndaelSBox


def TranslateToSBox(Spalte): #Erhalte einen eindimensionalen Array mit 4 Werten.
	
	Translated = list()
	for Wert in Spalte:
		fd = Wert[-2] #Erste Stelle
		sd = Wert[-1] #Zweite Stelle
		
		fd = int(fd , 16)
		sd = int(sd , 16)

		output = RijndaelSBox.SBox[fd]
		Translated.append(hex(output[sd]))
	print(Translated)
	return Translated
	
def BlockSubBytes(Block):
	#Hole eine Spalte aus dem Block
	for i in range(0,4,1):
		Block[i] = TranslateToSBox(Block[i])
	return Block
	


Block = list()
Block.append([0x19, 0xa0, 0x9a, 0xe9])
Block.append([0x3d, 0xf4, 0xc6, 0xf8])
Block.append([0xe3, 0xe2, 0x8d, 0x48])
Block.append([0xbe, 0x2b, 0x2a, 0x08])

for Spalte in Block:
    for i in range(0,4):
        Spalte[i] = format(Spalte[i], '#04x')

Block = BlockSubBytes(Block)
for Spalte in Block:
	print(Spalte)
