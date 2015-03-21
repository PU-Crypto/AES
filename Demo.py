#So werden die verschiedenen Tabellen beispielhaft eingebunden:
from Tables import RijndaelSBox
from Tables import RijndaelRcon
from Tables import MixColumnsTables

output = RijndaelSBox.SBox[2]
print(output[0])

print(RijndaelRcon.Rcon[1])

output = MixColumnsTables.TableL[0]
print(output[2])