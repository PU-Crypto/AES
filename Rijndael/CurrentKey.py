def GetCurrentKey(runde, key): # Ermittle aus dem recht langen Key Array die aktuell noetigen Werte (4x4)
	output = list()
	for i in range(runde,runde+4):
		output.append(key[i])
	return output