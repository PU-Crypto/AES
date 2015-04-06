from Rijndael.Tables import MixColumnsTables


def LLesen(leseWert): #Anhand des ersten Zeichens (fd, vertikal) und des zweiten Zeichens (sd, horizontal) wird die Logarithmustabelle ausgelesen
    leseWert = str(leseWert)
    fd = int(leseWert[-2],16)
    sd = int(leseWert[-1],16)
    dump = MixColumnsTables.TableL[fd]
    output = dump[sd]
    output = hex(output).split('x')[1]
    return output


def ELesen(leseWert): #Anhand des ersten Zeichens (fd, vertikal) und des zweiten Zeichens (sd, horizontal) wird die Exponentialtabelle ausgelesen
    leseWert = str(leseWert)
    if len(leseWert) < 2: #Wenn der lesewert nur einstellig ist, ist eine 0 davor, welche beim Auslesen beachtet werden muss.
        leseWert = str(str(0) + leseWert)
    fd = int(leseWert[-2],16)
    sd = int(leseWert[-1],16)
    dump = MixColumnsTables.TableE[fd]
    output = dump[sd]
    return output

    
def Multi(Faktor1,Faktor2): #Fuehre die Multiplikation im Galouiskoerper aus, mit Hilfe der Vereinfachung durch eine Addition der Werte aus der Exponentialtabelle und der Logarithmustabelle durch
    if Faktor1 =='0x00': #Wenn der Faktor 0 ist, ist das Ergebnis auch im Galouiskoerper 0 daher wird die Funktion hier beendet
        return int('0x00',16)
    Faktor1 = str(LLesen(Faktor1))
    Faktor2 = str(LLesen(Faktor2))
    Summe = int(Faktor1,16) + int(Faktor2,16)
    if Summe > 255:
        Summe = Summe - 255
    Summe = hex(Summe).split('x')[1]
    output = int(hex(ELesen(Summe)),16)
    return output
    
def MixColumns(eingabeBlock = []): #Multipliziere und Verknuepfe XOR mit einer gegebenen Matrix auf Basis des Galouiskoerpers; Rueckgabeformat: Array mit Werten: 0x..
    Zeile = eingabeBlock[0]
    Zeile1 = eingabeBlock[1]
    Zeile2 = eingabeBlock[2]
    Zeile3 = eingabeBlock[3]
    a = format(Multi(Zeile[0],'02')^Multi(Zeile1[0],'03')^Multi(Zeile2[0],'01')^Multi(Zeile3[0],'01'), '#04x')
    b = format(Multi(Zeile[1],'02')^Multi(Zeile1[1],'03')^Multi(Zeile2[1],'01')^Multi(Zeile3[1],'01'), '#04x')
    c = format(Multi(Zeile[2],'02')^Multi(Zeile1[2],'03')^Multi(Zeile2[2],'01')^Multi(Zeile3[2],'01'), '#04x')
    d = format(Multi(Zeile[3],'02')^Multi(Zeile1[3],'03')^Multi(Zeile2[3],'01')^Multi(Zeile3[3],'01'), '#04x')
    
    e = format(Multi(Zeile[0],'01')^Multi(Zeile1[0],'02')^Multi(Zeile2[0],'03')^Multi(Zeile3[0],'01'), '#04x')
    f = format(Multi(Zeile[1],'01')^Multi(Zeile1[1],'02')^Multi(Zeile2[1],'03')^Multi(Zeile3[1],'01'), '#04x')
    g = format(Multi(Zeile[2],'01')^Multi(Zeile1[2],'02')^Multi(Zeile2[2],'03')^Multi(Zeile3[2],'01'), '#04x')
    h = format(Multi(Zeile[3],'01')^Multi(Zeile1[3],'02')^Multi(Zeile2[3],'03')^Multi(Zeile3[3],'01'), '#04x')
    
    i = format(Multi(Zeile[0],'01')^Multi(Zeile1[0],'01')^Multi(Zeile2[0],'02')^Multi(Zeile3[0],'03'), '#04x')
    j = format(Multi(Zeile[1],'01')^Multi(Zeile1[1],'01')^Multi(Zeile2[1],'02')^Multi(Zeile3[1],'03'), '#04x')
    k = format(Multi(Zeile[2],'01')^Multi(Zeile1[2],'01')^Multi(Zeile2[2],'02')^Multi(Zeile3[2],'03'), '#04x')
    l = format(Multi(Zeile[3],'01')^Multi(Zeile1[3],'01')^Multi(Zeile2[3],'02')^Multi(Zeile3[3],'03'), '#04x')

    m = format(Multi(Zeile[0],'03')^Multi(Zeile1[0],'01')^Multi(Zeile2[0],'01')^Multi(Zeile3[0],'02'), '#04x')
    n = format(Multi(Zeile[1],'03')^Multi(Zeile1[1],'01')^Multi(Zeile2[1],'01')^Multi(Zeile3[1],'02'), '#04x')
    o = format(Multi(Zeile[2],'03')^Multi(Zeile1[2],'01')^Multi(Zeile2[2],'01')^Multi(Zeile3[2],'02'), '#04x')
    p = format(Multi(Zeile[3],'03')^Multi(Zeile1[3],'01')^Multi(Zeile2[3],'01')^Multi(Zeile3[3],'02'), '#04x')
    ausgabeBlock = []
    ausgabeBlock.append([a,b,c,d])
    ausgabeBlock.append([e,f,g,h])
    ausgabeBlock.append([i,j,k,l])
    ausgabeBlock.append([m,n,o,p])
    
    return ausgabeBlock
    
def DeMixColumns(eingabeBlock = []): #Multipliziere und Verknuepfe XOr mit einer gegebenen Matrix auf Basis des Galouiskoerpers, diese ist die Inverse Matrix zur Verschlüsselungsmatrix; Rueckgabeformat: Array mit Werten: 0x..
    Zeile = eingabeBlock[0]
    Zeile1 = eingabeBlock[1]
    Zeile2 = eingabeBlock[2]
    Zeile3 = eingabeBlock[3]
    a = format(Multi(Zeile[0],'0e')^Multi(Zeile1[0],'0b')^Multi(Zeile2[0],'0d')^Multi(Zeile3[0],'09'), '#04x')
    b = format(Multi(Zeile[1],'0e')^Multi(Zeile1[1],'0b')^Multi(Zeile2[1],'0d')^Multi(Zeile3[1],'09'), '#04x')
    c = format(Multi(Zeile[2],'0e')^Multi(Zeile1[2],'0b')^Multi(Zeile2[2],'0d')^Multi(Zeile3[2],'09'), '#04x')
    d = format(Multi(Zeile[3],'0e')^Multi(Zeile1[3],'0b')^Multi(Zeile2[3],'0d')^Multi(Zeile3[3],'09'), '#04x')
    
    e = format(Multi(Zeile[0],'09')^Multi(Zeile1[0],'0e')^Multi(Zeile2[0],'0b')^Multi(Zeile3[0],'0d'), '#04x')
    f = format(Multi(Zeile[1],'09')^Multi(Zeile1[1],'0e')^Multi(Zeile2[1],'0b')^Multi(Zeile3[1],'0d'), '#04x')
    g = format(Multi(Zeile[2],'09')^Multi(Zeile1[2],'0e')^Multi(Zeile2[2],'0b')^Multi(Zeile3[2],'0d'), '#04x')
    h = format(Multi(Zeile[3],'09')^Multi(Zeile1[3],'0e')^Multi(Zeile2[3],'0b')^Multi(Zeile3[3],'0d'), '#04x')
    
    i = format(Multi(Zeile[0],'0d')^Multi(Zeile1[0],'09')^Multi(Zeile2[0],'0e')^Multi(Zeile3[0],'0b'), '#04x')
    j = format(Multi(Zeile[1],'0d')^Multi(Zeile1[1],'09')^Multi(Zeile2[1],'0e')^Multi(Zeile3[1],'0b'), '#04x')
    k = format(Multi(Zeile[2],'0d')^Multi(Zeile1[2],'09')^Multi(Zeile2[2],'0e')^Multi(Zeile3[2],'0b'), '#04x')
    l = format(Multi(Zeile[3],'0d')^Multi(Zeile1[3],'09')^Multi(Zeile2[3],'0e')^Multi(Zeile3[3],'0b'), '#04x')

    m = format(Multi(Zeile[0],'0b')^Multi(Zeile1[0],'0d')^Multi(Zeile2[0],'09')^Multi(Zeile3[0],'0e'), '#04x')
    n = format(Multi(Zeile[1],'0b')^Multi(Zeile1[1],'0d')^Multi(Zeile2[1],'09')^Multi(Zeile3[1],'0e'), '#04x')
    o = format(Multi(Zeile[2],'0b')^Multi(Zeile1[2],'0d')^Multi(Zeile2[2],'09')^Multi(Zeile3[2],'0e'), '#04x')
    p = format(Multi(Zeile[3],'0b')^Multi(Zeile1[3],'0d')^Multi(Zeile2[3],'09')^Multi(Zeile3[3],'0e'), '#04x')
    ausgabeBlock = []
    ausgabeBlock.append([a,b,c,d])
    ausgabeBlock.append([e,f,g,h])
    ausgabeBlock.append([i,j,k,l])
    ausgabeBlock.append([m,n,o,p])
    
    return ausgabeBlock