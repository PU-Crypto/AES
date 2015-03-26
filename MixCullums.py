from Tables import MixColumnsTables
import math 

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
    
def XOR(zblock = []):
    block = zblock[0]
    block1 = zblock[1]
    block2 = zblock[2]
    block3 = zblock[3]
    a = hex(Multi(hex(block[0]),'02')^Multi(hex(block1[0]),'03')^Multi(hex(block2[0]),'01')^Multi(hex(block3[0]),'01'))
    b = hex(Multi(hex(block[1]),'02')^Multi(hex(block1[1]),'03')^Multi(hex(block2[1]),'01')^Multi(hex(block3[1]),'01'))
    c = hex(Multi(hex(block[2]),'02')^Multi(hex(block1[2]),'03')^Multi(hex(block2[2]),'01')^Multi(hex(block3[2]),'01'))
    d = hex(Multi(hex(block[3]),'02')^Multi(hex(block1[3]),'03')^Multi(hex(block2[3]),'01')^Multi(hex(block3[3]),'01'))
    
    e = hex(Multi(hex(block[0]),'01')^Multi(hex(block1[0]),'02')^Multi(hex(block2[0]),'03')^Multi(hex(block3[0]),'01'))    
    f = hex(Multi(hex(block[1]),'01')^Multi(hex(block1[1]),'02')^Multi(hex(block2[1]),'03')^Multi(hex(block3[1]),'01'))
    g = hex(Multi(hex(block[2]),'01')^Multi(hex(block1[2]),'02')^Multi(hex(block2[2]),'03')^Multi(hex(block3[2]),'01'))
    h = hex(Multi(hex(block[3]),'01')^Multi(hex(block1[3]),'02')^Multi(hex(block2[3]),'03')^Multi(hex(block3[3]),'01'))    
    
    i = hex(Multi(hex(block[0]),'01')^Multi(hex(block1[0]),'01')^Multi(hex(block2[0]),'02')^Multi(hex(block3[0]),'03'))
    j = hex(Multi(hex(block[1]),'01')^Multi(hex(block1[1]),'01')^Multi(hex(block2[1]),'02')^Multi(hex(block3[1]),'03'))
    k = hex(Multi(hex(block[2]),'01')^Multi(hex(block1[2]),'01')^Multi(hex(block2[2]),'02')^Multi(hex(block3[2]),'03'))
    l = hex(Multi(hex(block[3]),'01')^Multi(hex(block1[3]),'01')^Multi(hex(block2[3]),'02')^Multi(hex(block3[3]),'03'))

    m = hex(Multi(hex(block[0]),'03')^Multi(hex(block1[0]),'01')^Multi(hex(block2[0]),'01')^Multi(hex(block3[0]),'02'))
    n = hex(Multi(hex(block[1]),'03')^Multi(hex(block1[1]),'01')^Multi(hex(block2[1]),'01')^Multi(hex(block3[1]),'02'))
    o = hex(Multi(hex(block[2]),'03')^Multi(hex(block1[2]),'01')^Multi(hex(block2[2]),'01')^Multi(hex(block3[2]),'02'))
    p = hex(Multi(hex(block[3]),'03')^Multi(hex(block1[3]),'01')^Multi(hex(block2[3]),'01')^Multi(hex(block3[3]),'02'))
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
    
op = []
op.append([0xd4, 0xe0, 0xb8, 0x1e])
op.append([0xbf, 0xb4, 0x41, 0x27])
op.append([0x5d, 0x52, 0x11, 0x98])
op.append([0x30, 0xae, 0xf1, 0xe5])

    
r = op[0]
s = op[1]
t = op[2]
u = op[3]
a = hex(Multi(hex(r[0]),'02')^Multi(hex(s[0]),'03')^Multi(hex(t[0]),'01')^Multi(hex(u[0]),'01'))  
print(XOR(op))

    



