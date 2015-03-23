def Padding(string):
	while(len(string)%8!=0):
		string+='0'
	return string

s='drölfzigtausendzweihundertsechsundsechzig'
s=s.encode('utf-8')
list(s)
#print(s)
sammlung = []
for i in range(0,len(s)): #erstelle einen array mit zahlen 
        dump=s[i]
        sammlung.append(dump)
print(sammlung)

einString =''
for i in range(0,len(sammlung)): #erstelle einen array mit dualzahlen
	einString+="{0:b}".format(sammlung[i])

print(einString)

einString = Padding(einString) ##Ergaenze den string um 0 bis er durch 8 teilbar ist

block=list()
for i in range(0,len(einString),8): #teile in 8er Bloecke
	dump=''
	for j in range(i,i+8):
		dump+=einString[j]
	block.append(dump)

#callCBC
print(block)