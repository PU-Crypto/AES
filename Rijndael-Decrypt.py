import Utility.UTF8_Convert as UTF8
import Utility.CBC as CBC
from Rijndael.KeySchedule import KeySchedule as KeySchedule
from Rijndael.AddRoundKey import AddRoundKey as AddRoundKey
from Rijndael.SubBytes import InvSubBytes as InvSubBytes
from Rijndael.ShiftRows import DeShiftRows as DeShiftRows
from Rijndael.MixColumns import DeMixColumns as DeMixColumns

def GetCurrentKey(runde, key): # Ermittle aus dem recht langen Key Array die aktuell noetigen Werte
	output = list()
	for i in range(runde,runde+4):
		output.append(key[i])
	return output

def RijndaelDecrypt(cipher, key): #cipher ist ein 4x4 Block(zeilenorientiert) mit Hexadezimalwerten im Format 0x.. ; key ist der bereits erweiterte Key
	text = list() #Der letztendlich entschluesselte Text

	#Die erste Runde der Entschluesselung: Die Verschluesselung Rueckwaerts
	firstKey = GetCurrentKey(40, key)
	text = AddRoundKey(firstKey, cipher)
	text = DeShiftRows(text)
	text = InvSubBytes(text)
	
	#Ausfuehrung der 9 vollstaendigen Runden andersherum als bei der Verschlüsellung die range kommt durch GetCurrentKey zustande
	for i in range(36, 3, -4):
		currentKey = GetCurrentKey(i, key)
		text = AddRoundKey(currentKey, text)

		text = DeMixColumns(text)
		text = DeShiftRows(text)
		text = InvSubBytes(text)

	text = AddRoundKey(key, text)

	return text




cipher = [['0x2f', '0x07', '0xbf', '0xac'], ['0xeb', '0x48', '0x80', '0x5f'], ['0xcf', '0x4a', '0xef', '0x4a'], ['0x7b', '0xaf', '0xd3', '0xb7'], ['0x7a', '0xd7', '0x4c', '0xf5'], ['0x57', '0x68', '0x0a', '0xce'], ['0xaf', '0x5c', '0x81', '0xa7'], ['0xbb', '0x37', '0x98', '0x1d']]
key = list() #Beispiel
key.append(['0x2b', '0x7e', '0x15', '0x16'])
key.append(['0x28', '0xae', '0xd2', '0xa6'])
key.append(['0xab', '0xf7', '0x15', '0x88'])
key.append(['0x09', '0xcf', '0x4f', '0x3c'])

key = KeySchedule(key)

Block4x4 = list()
decrypted = list()
for i in range(0,len(cipher)):
	Block4x4.append(cipher[i])
	if len(Block4x4) == 4:

		decrypted.append(RijndaelDecrypt(Block4x4, key)) #Uebergib den 4x4 Block an Rijndael
		
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
print(plain) #Gib das entschluesselte Ergebnis aus
