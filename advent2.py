file = open("./data/advent2data.txt","r")
lines = file.readlines()

for line in lines:
	maxmin, letter, s = line.split(" ")
	min, max = maxmin.split("-")
	letter = letter[0]
	print(max, min ,letter)
