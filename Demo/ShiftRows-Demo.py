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
 

op = []
op.append(['a','b','c','d'])
op.append(['a','b','c','d'])
op.append(['a','b','c','d'])
op.append(['a','b','c','d'])
print(ShiftRows(op))