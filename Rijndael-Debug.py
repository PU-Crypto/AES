 # -*- coding: utf-8 -*-
 #Nutzung:
 # mit -m={d,e} {Entschluesselung, Verschluesselung}
 # mit -p=<Passwort>
 # mit -t=Text --> Der Text darf keine Leerzeichen enthalten
import sys
import Utility.UTF8_Convert as UTF8
import Utility.CBC as CBC
import Utility.KeyGen as KeyGen
from Rijndael.CurrentKey import GetCurrentKey as GetCurrentKey
from Rijndael.KeySchedule import KeySchedule as KeySchedule
from Rijndael.AddRoundKey import AddRoundKey as AddRoundKey
from Rijndael.SubBytes import SubBytes as SubBytes
from Rijndael.ShiftRows import ShiftRows as ShiftRows
from Rijndael.MixColumns import MixColumns as MixColumns
from Rijndael.SubBytes import InvSubBytes as InvSubBytes
from Rijndael.ShiftRows import DeShiftRows as DeShiftRows
from Rijndael.MixColumns import DeMixColumns as DeMixColumns



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
	key = KeySchedule(key) #Erweitere den Schluessel
	plain = UTF8.UTFConvert(text)
	RijndaelBlock = CBC.GenRijndaelBlock(plain) # Wende CBC an und forme Listen mit 4 Hexadezimalwerten
	
	Block4x4 = list() #Forme 4x4 Bloecke und uebergib sie an Rijndael
	preciphertext = list()
	for i in range(0,len(RijndaelBlock)):
		Block4x4.append(RijndaelBlock[i])
		if len(Block4x4) == 4:
			encrypted = RijndaelRechnung(Block4x4, key) #Uebergib den 4x4 Block an Rijndael
			for Zeile in encrypted:
				preciphertext.append(Zeile)
			Block4x4 = list()
	ciphertext = ''
	for Zeile in preciphertext:
		for Wert in Zeile:
			Wert = Wert.split('x')[1]
			ciphertext += Wert	
	return ciphertext

def RijndaelDecryptRechnung(cipher, key): #cipher ist ein 4x4 Block(zeilenorientiert) mit Hexadezimalwerten im Format 0x.. ; key ist der bereits erweiterte Schluessel
	text = list() #Der letztendlich entschluesselte Text

	#Die erste Runde der Entschluesselung: Die Verschluesselung Rueckwaerts angeordnet
	firstKey = GetCurrentKey(40, key)
	text = AddRoundKey(firstKey, cipher)
	text = DeShiftRows(text)
	text = InvSubBytes(text)
	
	#Ausfuehrung der 9 vollstaendigen Runden andersherum als bei der Verschluessellung. Die range kommt durch GetCurrentKey zustande, ebenfalls invers zur Verschluesselung
	for i in range(36, 3, -4):
		currentKey = GetCurrentKey(i, key)
		text = AddRoundKey(currentKey, text)

		text = DeMixColumns(text)
		text = DeShiftRows(text)
		text = InvSubBytes(text)

	text = AddRoundKey(key, text)

	return text




def RijndaelDecrypt(cipher,password): #Entschluessel mit dem Passwort und dem Cipher
	precipher = list(cipher) #Schreibt Cipher in eine Liste
	HexArray = list()
	for i in range (0,len(precipher),2): #Macht die einzelnen Eintraege zu 0xAB - Eintraegen
		paar = '0x' + precipher[i] + precipher[i+1]
		HexArray.append(paar)
	dump = list()
	cipher = list()
	for i in range(0,len(HexArray)): #Mach den X-Array zu einem Xx4-Array
		dump.append(HexArray[i])
		if len(dump) == 4:
			cipher.append(dump)
			dump = list()
	
	key = KeyGen.KeyGen(password) #generiert den Key aus dem Passwort
	key = KeySchedule(key) #erweitert den Key
	
	Block4x4 = list()
	decrypted = list()
	for i in range(0,len(cipher)): #macht 4x4 Bloecke
		Block4x4.append(cipher[i])
		if len(Block4x4) == 4:
			decrypted.append(RijndaelDecryptRechnung(Block4x4, key)) #Uebergib den 4x4 Block an Rijndael
			Block4x4 = list()
	
	#Entferne die Bloecke und forme ein Liste aus einzelnen Werten
	decryptedList = list()
	for Block in decrypted:
		for Zeile in Block:
			for Wert in Zeile:
				decryptedList.append(Wert)
	#decryptedList = CBC.CBC_Decrypt(decryptedList)#Mache CBC rueckgaengig
	plain = list()
	for wert in decryptedList:
		wert = "{0:b}".format(int(wert,16))
		wert = UTF8.Padding(wert,8) #Stelle das alte 8-stellige Format wieder her
		plain.append(wert)
	text=UTF8.UTFdeConvert(plain) #Erstelle aus den Zahlen nach der UTF-Tabelle Buchstaben
	return text#Gib das entschluesselte Ergebnis aus

def handleShellParam(param, default):

	for cmdarg in sys.argv:
		if(("--" + param + "=") in cmdarg):
			return str(cmdarg.replace(("--" + param + "="), ""))
		elif(("-" + param + "=") in cmdarg):
			return str(cmdarg.replace(("-" + param + "="), ""))
		elif(("--" + param) in cmdarg):
			return str(cmdarg.replace(("--"), ""))
		elif(("-" + param) in cmdarg):
			return str(cmdarg.replace(("-"), ""))
	return default

def checkResult(textIn, encrypted, password): #Nimm den Eingangstext und den Verschlüsselten Text und versuche beide zu vergleichen
	try:
		decrypted = RijndaelDecrypt(encrypted, password)
		if decrypted == textIn:
			return True
		else:
			#e = sys.exc_info()[0]
			#print("Error in run: \n" + str(e))
			return False
	except:
		e = sys.exc_info()[0]
		print("Error in run: \n" + str(e))
		return False

mode = handleShellParam("m", 0) 
#Zur Bestimmung was gerade von dem Script verlangt wird, sonst exited er, wenn man verschluesseln will und natuerlich das Password fehlt fuer Encrypt die 1 und fuer Decrypt die 2
password = handleShellParam("p", 0)
text = handleShellParam("t", 0)

#mode='e'
#password='StrengstensGeheim'
#if mode=='e':
#	text='eivaejooheepiyahshogahqu'
#else:
#	text='230e564c7ff6099750826e0a1b97e8c729de59d7927b3ce13d67441a2bf051f2'

if mode == 'e':
	if password == 0 or text == 0:
		print('Bitte fuellen Sie sowohl Password als auch Entschluesselungsfeld aus')
		sys.exit(1)
	
	if password != 0 and text != 0:
		password += 'saltibus#Minnimax' #Salte das Passwort

		loopprevent=0
		while(loopprevent < 3): #Teste ob die Verschluesselung funktioniert hat sollte loopprevent ausschlagen gib eine Fehlermeldung aus
			encrypted = Rijndael(text, password)
			if checkResult(text,encrypted,password):
				print(encrypted)
				break;
			loopprevent += 1
			print()
		if loopprevent == 4:
			print("Dieser Text konnte nicht verschluesselt werden")
			sys.exit(1)
		sys.exit(0)

if mode == 'd':
	if password!=0 and text != 0:
		password += 'saltibus#Minnimax'
		try:
			decrypted = RijndaelDecrypt(text, password)
			print(decrypted)
		except:
			e = sys.exc_info()[0]
			print("Error in run: \n" + str(e))
			sys.exit(1)
		sys.exit(0)
	if password == 0 or text == 0:
		print('Bitte fuellen sie sowohl Password als auch Verschluesselungsfeld aus')
		sys.exit(1)

if mode == 0:
	exit("Bitte geben Sie an, ob Ver- oder Entschluesselt werden soll \n Verschluesselung : e \n Entschluesselung : d")
