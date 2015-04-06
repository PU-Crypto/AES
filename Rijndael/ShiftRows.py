#Verschiebe die Werte in der Zeile in Abhaengigkeit des Indizes der Zeile
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
 
def DeShiftRows(Block):
    for i in range(0,4):
        Zeile = Block[i]
        for n in range(0,i):
            dump =[]
            dump.append(Zeile[3])      #Inverse Vertauschung
            dump.append(Zeile[0])
            dump.append(Zeile[1])
            dump.append(Zeile[2])
            Zeile = dump
        Block[i] = Zeile
    return Block

text  = list() #Beispiel
text.append(['0x32', '0x88', '0x31', '0xe0'])
text.append(['0x43', '0x5a', '0x31', '0x37'])
text.append(['0xf6', '0x30', '0x98', '0x07'])
text.append(['0xa8', '0x8d', '0xa2', '0x34'])

test = ShiftRows(text)
#print(DeShiftRows(test))

