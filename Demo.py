#So werden die verschiedenen Tabellen beispielhaft eingebunden:
from Tables import RijndaelSBox
from Tables import RijndaelRconField

output = RijndaelSBox.SBox[2]
print(output[0])

print(RijndaelRconField.Rcon[1])