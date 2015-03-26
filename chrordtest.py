def Padding(string,laenge):
	while(len(string)%laenge!=0):
		string='0' + string 
	return string

def SplitBlocks(einString,Splitter):
	block=list()
	for i in range(0,len(einString),Splitter): #teile in 8er Bloecke
		dump=''
		for j in range(i,i+Splitter):
			dump+=einString[j]
		block.append(dump)
	return block


#plain='Dies ist ein sehr langer text, da mich interessiert ob er vielleicht irentwann abkack und mir mitteilt, dass er mit seinem Latein am ende ist. Fürgt er eigenlich schon alles unten zu einem Text zusammen? Naja ich werde es gleich sehen dnke ich. Meinst du das reicht schon an text? Ich glabe ich höre jetzt auf.'
def UTFConvert(plain):
    s=list(plain)
    for i in range(0,len(s)):
        s[i]=ord(s[i])

    #print(s)
    #print(type(s))
#print(type(plain))
    einString =''
    for i in range(0,len(s)): #erstelle einen array mit dualzahlen
        dump = "{0:b}".format(s[i])
        dump = Padding(dump,11)
        einString += dump

#print(einString)

    einString = Padding(einString,8) ##Ergaenze den string um 0 bis er durch 8 teilbar ist

    block = SplitBlocks(einString,8)

    #callCBC
    #print(block)

    leerevariable = ''
    for i in range(0,len(block)):
        leerevariable+=block[i]
    return leerevariable




def UTFdeConvert(leerevariable):
    leerevariable= str(int(leerevariable))
    leerevariable = Padding(leerevariable,11)
    #print(leerevariable)
    block=SplitBlocks(leerevariable,11)

#print(block)

    Zahlen = list()
    for wert in block:
        wert = int(wert,2)
        #print(wert)
        wert = chr(wert)
        #print(wert)
        Zahlen.append(wert)

#print(type(Zahlen[0]))
#print(Zahlen)
    ausString =''
    for i in range(0,len(Zahlen)): #erstelle einen array mit dualzahlen
        ausString += Zahlen[i]
#        print(ausString)
    return ausString


