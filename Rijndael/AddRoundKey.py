def AddRoundKey(key, text): #Verknuepfe den text und den key der Runde XOR
    output = list()
    for i in range(0,4):
        Zeile = list()
        for n in range(0,4):
            TextZeile=text[i]
            KeySpalte=key[n]
            Zeile.append(format(int(TextZeile[n],16)^int(KeySpalte[i],16), '#04x'))
        output.append(Zeile)
    return output