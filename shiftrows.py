Block=[]
for i in range(0,4):
	Zeile=Block[i]
	#dump=Block[i]		#wozu ist dieser schritt gut? rall ich grade nicht.
	for n in range(0,n):
		dump[0] = Zeile[1]
		dump[1] = Zeile[2]
		dump[2] = Zeile[3]
		dump[3] = Zeile[0]
	Block[i] = dump