import Utility.UTF8_Convert as UTF8
import Utility.CBC as CBC
import Utility.KeyGen as KeyGen
from Rijndael.CurrentKey import GetCurrentKey as GetCurrentKey
from Rijndael.KeySchedule import KeySchedule as KeySchedule
from Rijndael.AddRoundKey import AddRoundKey as AddRoundKey
from Rijndael.SubBytes import InvSubBytes as InvSubBytes
from Rijndael.ShiftRows import DeShiftRows as DeShiftRows
from Rijndael.MixColumns import DeMixColumns as DeMixColumns

def RijndaelDecryptRechnung(cipher, key): #cipher ist ein 4x4 Block(zeilenorientiert) mit Hexadezimalwerten im Format 0x.. ; key ist der bereits erweiterte Schluessel
	text = list() #Der letztendlich entschluesselte Text

	#Die erste Runde der Entschluesselung: Die Verschluesselung Rueckwaerts angeordnet
	firstKey = GetCurrentKey(40, key)
	text = AddRoundKey(firstKey, cipher)
	text = DeShiftRows(text)
	text = InvSubBytes(text)
	
	#Ausfuehrung der 9 vollstaendigen Runden andersherum als bei der Verschlüsellung. Die range kommt durch GetCurrentKey zustande, ebenfalls invers zur verschlüsselung
	for i in range(36, 3, -4):
		currentKey = GetCurrentKey(i, key)
		text = AddRoundKey(currentKey, text)

		text = DeMixColumns(text)
		text = DeShiftRows(text)
		text = InvSubBytes(text)

	text = AddRoundKey(key, text)

	return text




def RijndaelDecrypt(cipher,password): #Entschluessel mit Passwort und dem dem Cipher
	precipher = list(cipher) #schreibt Cipher in eine Liste
	HexArray =[]
		
	for i in range (0,len(precipher),2): #macht die einzelnen eintäge zu 0xAB - Einträge
		paar = '0x' + precipher[i] + precipher[i+1]
		HexArray.append(paar)
	dump = []
	cipher = []
	for i in range(0,len(HexArray)): #Mach den X-Array zu einem Xx4-Array
		dump.append(HexArray[i])
		if len(dump) == 4:
			cipher.append(dump)
			dump = list()
	key = KeyGen.KeyGen(password) #generiert den Key aus dem Passwort
	key = KeySchedule(key) #erweitert den Key
	
	Block4x4 = list()
	decrypted = list()
	for i in range(0,len(cipher)): #macht 4x4 Blöcke
		Block4x4.append(cipher[i])
		if len(Block4x4) == 4:
	
			decrypted.append(RijndaelDecryptRechnung(Block4x4, key)) #Uebergib den 4x4 Block an Rijndael
			
			Block4x4 = list()
	
	#Entferne die Bloecke und forme ein Liste aus einzelnen Werten und entferne reine 0 Bloecke
	
	decryptedList = list()
	for Block in decrypted:
		for Zeile in Block:
			for Wert in Zeile:
				if Wert != '0x00':
					decryptedList.append(Wert)
	
	plain = CBC.CBC_Decrypt(decryptedList)#Mache CBC rueckgaengig
	plain=UTF8.UTFdeConvert(plain) #Erstelle aus den Zahlen nach der UTF-Tabelle Buchstaben
	return plain#Gib das entschluesselte Ergebnis aus
a = 'a21cd3521371ff7e3848e2b6107793c3f0b943fc17c8c7615dfe6239c421755df20866db64b27dcd5e4fb33f6237e930'
b = 'das ist mein passwort'
print(RijndaelDecrypt(a,b))