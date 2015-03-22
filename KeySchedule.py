#KeySchedule
import SubBytes
from Tables import RijndaelRcon

def RotWord(Spalte):
        #Verschiebe die Plaetze im Array

def KeySchedule(Cipher):
        for i in range(4,40,4):
            Cipher[i] = RotWord(Cipher[i-1]])
            Cipher[i] = SubBytes.TranslateToSBox(Cipher[i-1])
            Cipher[i] = Cipher[i-4]^Cipher[i]^RijndaelRcon.Rcon[(i/4)-1]    
