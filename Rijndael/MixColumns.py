from Rijndael.Tables import MixColumnsTables


def LLesen(ip):
    a = str(ip)
    fd = int(a[-2],16)
    sd = int(a[-1],16)
    output = MixColumnsTables.TableL[fd]
    e = output[sd]
    e = hex(e).split('x')[1]
    return e


def ELesen(ip):
    ip = str(ip)
    if len(ip) < 2:
        ip = str(str(0) + ip)
    fd = int(ip[-2],16)
    sd = int(ip[-1],16)
    output = MixColumnsTables.TableE[fd]
    y = output[sd]
    
    return y
    
def Multi(i,w):   
    a = str(LLesen(i))
    b = str(LLesen(w))
    c = int(a,16) + int(b,16)
    if c > 255:
        c = c - 255
    c = hex(c).split('x')[1]
    d = int(hex(ELesen(c)),16)
    return d
    
def MixColumns(zblock = []):
    block = zblock[0]
    block1 = zblock[1]
    block2 = zblock[2]
    block3 = zblock[3]
    a = hex(Multi(block[0],'02')^Multi(block1[0],'03')^Multi(block2[0],'01')^Multi(block3[0],'01'))
    b = hex(Multi(block[1],'02')^Multi(block1[1],'03')^Multi(block2[1],'01')^Multi(block3[1],'01'))
    c = hex(Multi(block[2],'02')^Multi(block1[2],'03')^Multi(block2[2],'01')^Multi(block3[2],'01'))
    d = hex(Multi(block[3],'02')^Multi(block1[3],'03')^Multi(block2[3],'01')^Multi(block3[3],'01'))
    
    e = hex(Multi(block[0],'01')^Multi(block1[0],'02')^Multi(block2[0],'03')^Multi(block3[0],'01'))    
    f = hex(Multi(block[1],'01')^Multi(block1[1],'02')^Multi(block2[1],'03')^Multi(block3[1],'01'))
    g = hex(Multi(block[2],'01')^Multi(block1[2],'02')^Multi(block2[2],'03')^Multi(block3[2],'01'))
    h = hex(Multi(block[3],'01')^Multi(block1[3],'02')^Multi(block2[3],'03')^Multi(block3[3],'01'))    
    
    i = hex(Multi(block[0],'01')^Multi(block1[0],'01')^Multi(block2[0],'02')^Multi(block3[0],'03'))
    j = hex(Multi(block[1],'01')^Multi(block1[1],'01')^Multi(block2[1],'02')^Multi(block3[1],'03'))
    k = hex(Multi(block[2],'01')^Multi(block1[2],'01')^Multi(block2[2],'02')^Multi(block3[2],'03'))
    l = hex(Multi(block[3],'01')^Multi(block1[3],'01')^Multi(block2[3],'02')^Multi(block3[3],'03'))

    m = hex(Multi(block[0],'03')^Multi(block1[0],'01')^Multi(block2[0],'01')^Multi(block3[0],'02'))
    n = hex(Multi(block[1],'03')^Multi(block1[1],'01')^Multi(block2[1],'01')^Multi(block3[1],'02'))
    o = hex(Multi(block[2],'03')^Multi(block1[2],'01')^Multi(block2[2],'01')^Multi(block3[2],'02'))
    p = hex(Multi(block[3],'03')^Multi(block1[3],'01')^Multi(block2[3],'01')^Multi(block3[3],'02'))
    nblock = []
    nblock.append([a,b,c,d])
    nblock.append([e,f,g,h])
    nblock.append([i,j,k,l])
    nblock.append([m,n,o,p])
    for i in range(0,4):
        u = nblock[i]
        for j in range(0,4):
            y = u[j]            
            if len(y) < 4:
                a,b = y.split('x')
                y = str(a + 'x' + str(0) + b)
                u[j] = y
    return nblock
    



    



