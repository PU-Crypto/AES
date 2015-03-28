def AddRoundKey(key, text): #Verknuepfe den Text und den Key der Runde XOR
    output = list()
    for i in range(0,4): #Erhoehe unterschiedlich von einander, um den Aufbau von Key und Text zu beachten ( Zeilen- vs. Spaltenorientiert)
        Zeile = list()
        for n in range(0,4):
            TextZeile=text[i]
            KeySpalte=key[n]
            Zeile.append(format(int(TextZeile[n],16)^int(KeySpalte[i],16), '#04x')) #Verknuepfe XOR und formatiere in Hexadezimal 0x..
        output.append(Zeile)
    return output