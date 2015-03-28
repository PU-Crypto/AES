import Utility.UTF8_Convert as UTF8
from Rijndael.KeySchedule import KeySchedule as KeySchedule
from Rijndael.AddRoundKey import AddRoundKey as AddRoundKey
from Rijndael.SubBytes import SubBytes as SubBytes
from Rijndael.ShiftRows import ShiftRows as ShiftRows
from Rijndael.MixColumns import MixColumns as MixColumns


def GetCurrentKey(runde, key): # Ermittle aus dem recht langen Key array die aktuell noetigen Werte
	output = list()
	for i in range(runde,runde+4):
		output.append(key[i])
	return output


text  = list()
text.append(['0x32', '0x88', '0x31', '0xe0'])
text.append(['0x43', '0x5a', '0x31', '0x37'])
text.append(['0xf6', '0x30', '0x98', '0x07'])
text.append(['0xa8', '0x8d', '0xa2', '0x34'])

key = list()
key.append(['0x2b', '0x7e', '0x15', '0x16'])
key.append(['0x28', '0xae', '0xd2', '0xa6'])
key.append(['0xab', '0xf7', '0x15', '0x88'])
key.append(['0x09', '0xcf', '0x4f', '0x3c'])

key = KeySchedule(key)

cipher = list() #Der letztendlich verschluesselte Text


cipher=AddRoundKey(key, text)

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

