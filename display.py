

# input
frequencies = [329, 262, 220, 175, 123, 87]


edict = {
  329 : "0",
  349 : "1",
  370 : "2",
  392 : "3",
  415 : "4",
  440 : "5",
}

Bdict = {
  247 : "0",
  262 : "1",
  277 : "2",
  294 : "3",
  311 : "4",
  #"B5": 329, same as e0
}

Gdict = {
  196 : "0",
  208 : "1",
  220 : "2",
  233 : "3",
  #"G4": 247, same as B0
  #"G5": 262, same as B1
}

Ddict = {
  147 : "0",
  156 : "1",
  165 : "2",
  175 : "3",
  185 : "4",
  #"D5": 196, same as G0
}

Adict = {
  110 : "0",
  117 : "1",
  123 : "2",
  131 : "3",
  139 : "4",
  #"A5": 147, same as D0
}

Edict = {
  82  : "0",
  87  : "1",
  92  : "2",
  98  : "3",
  104 : "4"
  #"E5": 110, same as A0
}

erow = "e " + "-"*len(frequencies)
Brow = "B " + "-"*len(frequencies)
Grow = "G " + "-"*len(frequencies)
Drow = "D " + "-"*len(frequencies)
Arow = "A " + "-"*len(frequencies)
Erow = "E " + "-"*len(frequencies)


rowlength = 5

for i in range(len(frequencies)):
	frequency = frequencies[i]

	# if (319 < frequency < 339)
		# frequency = 329;

	if(frequencies[i] in edict.keys()):
		erow = erow[0:i+2] + edict[frequencies[i]] + erow[i+3:rowlength+2]

	elif(frequencies[i] in Bdict.keys()):
		Brow = Brow[0:i+2] + Bdict[frequencies[i]] + Brow[i+3:rowlength+2]

	elif(frequencies[i] in Gdict.keys()):
		Grow = Grow[0:i+2] + Gdict[frequencies[i]] + Grow[i+3:rowlength+2]

	elif(frequencies[i] in Ddict.keys()):
		Drow = Drow[0:i+2] + Ddict[frequencies[i]] + Drow[i+3:rowlength+2]

	elif(frequencies[i] in Adict.keys()):
		Arow = Arow[0:i+2] + Adict[frequencies[i]] + Arow[i+3:rowlength+2]

	elif(frequencies[i] in Edict.keys()):
		Erow = Erow[0:i+2] + Edict[frequencies[i]] + Erow[i+3:rowlength+2]

# print(erow)
# print(Brow)
# print(Grow)
# print(Drow)
# print(Arow)
# print(Erow)


txtresult = open("test.txt", "w")
txtresult.write(erow + '\n' + 
				Brow + '\n' + 
				Grow + '\n' + 
				Drow + '\n' + 
				Arow + '\n' + 
				Erow + '\n')
txtresult.close()

#open and read the file after the appending:
txtresult = open("test.txt", "r")
print(txtresult.read())


