def decryptshiftrows(Block):		# name nochmal ueberdenken..
	for i in range(0,4):
		Zeile = Block[i]
		dump =[]
		for n in range(0,i):
			dump[1]	= Zeile[0]		# vertauschung in die andere richtung
			dump[2] = Zeile[1]
			dump[3] = Zeile[2]
			dump[0] = Zeile[3]
		Block[i] = dump
	return Block
