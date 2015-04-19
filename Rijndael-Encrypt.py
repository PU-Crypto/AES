import Utility.UTF8_Convert as UTF8
import Utility.CBC as CBC
from Rijndael.CurrentKey import GetCurrentKey as GetCurrentKey
from Rijndael.KeySchedule import KeySchedule as KeySchedule
from Rijndael.AddRoundKey import AddRoundKey as AddRoundKey
from Rijndael.SubBytes import SubBytes as SubBytes
from Rijndael.ShiftRows import ShiftRows as ShiftRows
from Rijndael.MixColumns import MixColumns as MixColumns


def Rijndael(text, key): #text ist ein 4x4 Block(zeilenorientiert) mit Hexadezimalwerten im Format 0x.. ; key ist der bereits erweiterte Key
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



text  = list() #Beispiel
text.append(['0x32', '0x88', '0x31', '0xe0'])
text.append(['0x43', '0x5a', '0x31', '0x37'])
text.append(['0xf6', '0x30', '0x98', '0x07'])
text.append(['0xa8', '0x8d', '0xa2', '0x34'])

key = list() #Beispiel
key.append(['0x2b', '0x7e', '0x15', '0x16'])
key.append(['0x28', '0xae', '0xd2', '0xa6'])
key.append(['0xab', '0xf7', '0x15', '0x88'])
key.append(['0x09', '0xcf', '0x4f', '0x3c'])

ciphertext = list()

key = KeySchedule(key) #Erweitere den Schluessel


plain = UTF8.UTFConvert('Ich mag Käse')
cipher = CBC.CBC_Encrypt(plain, '10101011')
RijndaelBlock = CBC.GenRijndaelBlock(cipher) #Forme Listen mit 4 Hexadezimalwerten

Block4x4 = list() #Forme 4x4 Bloecke und uebergib sie an Rijndael
for i in range(0,len(RijndaelBlock)):
	Block4x4.append(RijndaelBlock[i])
	if len(Block4x4) == 4:

		ciphertext.append(Rijndael(Block4x4, key)) #Uebergib den 4x4 Block an Rijndael
		
		Block4x4 = list()

print(ciphertext)