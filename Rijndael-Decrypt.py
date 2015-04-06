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
	#Ausfuehrung der 9 vollstaendigen Runden andersherum als bei der Verschlüsellung

	for i in range(36, 3, -4):
		currentKey = GetCurrentKey(i, key)
		text = AddRoundKey(currentKey, text)

		text = DeMixColumns(text)
		text = DeShiftRows(text)
		text = InvSubBytes(text)

	text = AddRoundKey(key, text)

	return text