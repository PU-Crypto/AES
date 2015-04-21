import Utility.Keccak as Keccak
myKeccak=Keccak.Keccak()


def KeyGen(string): 					#KeyGen macht aus einem Satz oder Passwort einen 4x4 Schlüsselarray
	s = list(string)
	einString =''
	for i in range(0,len(s)): 			#Jeden Zeichen der Eingabe wird über UTF8 übersetz und dann alle Hexadecimalzahlen zu einem String vereint
		s[i]=ord(s[i])
		dump = format(s[i],'#04x')
		dump = dump.split('x')[1]
		einString += dump

	sha3 = str(myKeccak.Keccak((128,einString),1152,448,224,True)) #dieser String wird mit Keccak (sha3) gehashed
	einzelListe = list(sha3) #dies ist die Liste der einzelnen Zeichen des Hash'
	zweierListe = []
	
	for n in range(0,4):     #die Einzelnen Zeichen werden als Zeichenpärchen zusammengefügt in einen 4x4 Array geschrieben
		zLZeile = []
		for i in range(0,8,2):
			paar = '0x' + einzelListe[i] + einzelListe[i+1]
			zLZeile.append(paar)
		zweierListe.append(zLZeile)
	output = zweierListe
	return output


