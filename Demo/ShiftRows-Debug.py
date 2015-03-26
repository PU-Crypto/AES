def ShiftRows(Block):		# Block ist der einzulesene Array
    for i in range(1,4):
        Zeile = Block[i]
        for n in range(0,i):
            dump = []            
            dump.append(Zeile[1])
            dump.append(Zeile[2])
            dump.append(Zeile[3])
            dump.append(Zeile[0])
            Zeile = dump
        Block[i] = Zeile
    return Block
 

Block = []

Block.append(['0xd4', '0xe0', '0xb8', '0x1e'])
Block.append(['0x27', '0xbf', '0xb4', '0x41'])
Block.append(['0x11', '0x98', '0x5d', '0x52'])
Block.append(['0xae', '0xf1', '0xe5', '0x30'])

Block = ShiftRows(Block)
print(Block)