def ShiftRows(Block):		# Block ist der einzulesene Array
	print(Block)
	for i in range(0,4):
		Zeile = Block[i]
		print(Zeile)
		dump = []
		for n in range(0,i):
			dump[0] = Zeile[1]
			dump[1] = Zeile[2]
			dump[2] = Zeile[3]
			dump[3] = Zeile[0]
		Block[i] = dump
	return Block

Block = []

Block.append(['0xd4', '0xe0', '0xb8', '0x1e'])
Block.append(['0x27', '0xbf', '0xb4', '0x41'])
Block.append(['0x11', '0x98', '0x5d', '0x52'])
Block.append(['0xae', '0xf1', '0xe5', '0x30'])

Block = ShiftRows(Block)
print(Block)