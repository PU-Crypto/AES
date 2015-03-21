#So werden die verschiedenen Tabellen beispielhaft eingebunden:
from Tables import RijndaelSBox
from Tables import RijndaelRcon

output = RijndaelSBox.SBox[2]
print(output[0])

print(RijndaelRcon.Rcon[1])