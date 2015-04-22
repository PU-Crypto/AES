import Utility.UTF8_Convert as UTF8
import Utility.CBC as CBC
import Utility.KeyGen as KeyGen
from Rijndael.CurrentKey import GetCurrentKey as GetCurrentKey
from Rijndael.KeySchedule import KeySchedule as KeySchedule
from Rijndael.AddRoundKey import AddRoundKey as AddRoundKey
from Rijndael.SubBytes import SubBytes as SubBytes
from Rijndael.ShiftRows import ShiftRows as ShiftRows
from Rijndael.MixColumns import MixColumns as MixColumns


def RijndaelRechnung(text, key): #text ist ein 4x4 Block(zeilenorientiert) mit Hexadezimalwerten im Format 0x.. ; key ist der bereits erweiterte Key
	cipher = list() #Der letztendlich verschluesselte Text
	
	
	cipher=AddRoundKey(key, text) #Durchfuehrung der Vorrunde

	
	#Ausfuehrung der 9 vollstaendigen Runden
	for i in range(4,37,4): #Erhoehe um 4 um Synchron zu den Schluesseln zu bleiben
		cipher = SubBytes(cipher)
		cipher = ShiftRows(cipher)
		cipher = MixColumns(cipher)
		
		currentKey = GetCurrentKey(i, key)
		cipher = AddRoundKey(currentKey, cipher)
	
	#Letzte Runde ohne MixColumns
	cipher = SubBytes(cipher)
	cipher = ShiftRows(cipher)
	lastKey = GetCurrentKey(40, key)
	cipher = AddRoundKey(lastKey, cipher)
	
	#Rueckgabe des verschluesselten Textes
	return cipher	 

def Rijndael(text,password):
	key = KeyGen.KeyGen(password) #generiere aus dem Passwort den Key
	preciphertext = list()
	key = KeySchedule(key) #Erweitere den Schluessel
	plain = UTF8.UTFConvert(text)
	cipher = CBC.CBC_Encrypt(plain, '10101011')
	RijndaelBlock = CBC.GenRijndaelBlock(cipher) #Forme Listen mit 4 Hexadezimalwerten
	
	Block4x4 = list() #Forme 4x4 Bloecke und uebergib sie an Rijndael
	for i in range(0,len(RijndaelBlock)):
		Block4x4.append(RijndaelBlock[i])
		if len(Block4x4) == 4:
			for j in range(0,4): #formt einen Xx4x4 Array in einen Xx4 Array
				a = RijndaelRechnung(Block4x4, key)
				preciphertext.append(a[j]) #Uebergib den 4x4 Block an Rijndael
			
			Block4x4 = list()
	ciphertext = ''
	for Zeile in preciphertext:
		for Wert in Zeile:
			Wert = Wert.split('x')[1]
			ciphertext += Wert
		
	return ciphertext
