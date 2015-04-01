import math
import UTF8_Convert as Utf8
def CBC_Encrypt(plain, key, initvektor): #Diese Funktion erwartet einen Plaintext, der Bereits mit Utf-8 Utility vorbereitet wurde und einen Key, der eine Zahl ist und ein Initialisierungsvektor, der Dual und 8 Steelen lang ist.
	if len(initvektor) < 8:
		exit()
	Block = list()
	Block.append(initvektor)
	for i in range(1, len(plain)):
		dump = "{0:b}".format(int(plain[i-1],2)^int(Block[i-1],2))
		if len(dump)< 8:
			dump = Utf8.Padding(dump, 8)
		Block.append(dump)
	return Block

plain = Utf8.UTFConvert('Ich mag Käse')
cipher = CBC_Encrypt(plain, bin(12345678), '10101011')
print(cipher)
for Objekt in cipher:
	print(Objekt)
	if len(Objekt) != 8:
		print(len(Objekt))