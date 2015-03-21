#So werden die verschiedenen Tabellen beispielhaft eingebunden:
from Tables import RijndaelSBox
from Tables import RijndaelRcon
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
    d = hex(ELesen(c))
    return d
e = Multi('02','d4')
f = Multi('03','32')

g = int('0xf4',16)
h = int('0xae',16)

#i = hex(g^h^f^e)
print(type(e))


    



