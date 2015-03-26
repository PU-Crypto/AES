def AddRoundKey(Key = [], Pretext = []):   
    for i in range(0,4):
        text1 = Pretext[i]
        key1 = Key[i]
        for j in range(0,4):
                text1[j] = hex(int(text1[j],16)^int(hex(key1[j]),16))
        Pretext[i] = text1
    for q in range(0,4):
        u = Pretext[q]
        for p in range(0,4):
            y = u[j]            
            if len(y) < 4:
                a,b = y.split('x')
                y = str(a + 'x' + str(0) + b)
                u[j] = y
    return Pretext 
    