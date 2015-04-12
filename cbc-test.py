import Utility.UTF8_Convert as UTF8
import Utility.CBC as CBC

plain = UTF8.UTFConvert('Ich mag Käse')

print(plain)
cipher = CBC.CBC_Encrypt(plain, bin(12345678), '10101011')
#print(cipher)
hexlist = list()
for Wert in cipher:
	dump = format(int(Wert,2),'#04x')
	hexlist.append(dump)
plain = CBC.CBC_Decrypt(hexlist)
print(plain)
plain = UTF8.UTFdeConvert(plain)

print(chr(0))
print(plain)