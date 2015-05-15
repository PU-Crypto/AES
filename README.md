Ordner
------
Rijndael: Die einzelnen Funktionen die Rijndael nutzt

Utility: Utf-8 Converter, CBC und Formatierungstools

AES-Script
----------

Rijndael.py:
------------
### Parameter:

### -m
e == Verschlüsselung
d == Entschlüsselung

### -p
Passwort

### -t
Der verschlüsselte oder der zu verschlüsselnde Text

Beispiel:
---------

* Verschluesselung
python Rijndael.py -m=e -p=EinSicheresPasswort -t=EinZuVerschluesselnderText

* Entschluesselung:
python Rijndael.py -m=d -p=EinSicheresPasswort -t=da751ce41e281105ae58dcb1f97108189bd5f6aa80f52bbf505130c3d6e0583226aa51fb1bb0a584abf8e97576658676