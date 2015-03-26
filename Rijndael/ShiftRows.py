def ShiftRows(Block):		# Block ist der einzulesene Array
	for i in range(0,4):
		Zeile = Block[i]
		dump = []
		for n in range(0,i):
			dump[0] = Zeile[1]
			dump[1] = Zeile[2]
			dump[2] = Zeile[3]
			dump[3] = Zeile[0]
		Block[i] = dump
	return Block