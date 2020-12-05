import math
file = open("./data/advent5data.txt","r")
lines = file.readlines()

#lines = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

airplane = [ [0 for x in range(8)] for y in range(128)]
#print(airplane)
maxNum = 0
for line in lines:
	prefix = line[:7]
	suffix = line[7:-1]
	fl = 0
	fr = 127
	for e in prefix:
		if e == "F":
			fr = math.floor((fr+fl)/2)
		elif e == "B":
			fl = math.ceil((fr+fl)/2)	
	
	p1 = 0
	p2 = 7
	for e in suffix:
		if e == "L":
			p2 = math.floor((p1+p2)/2)
		elif e == "R":
			p1 = math.ceil((p1+p2)/2)
	
	airplane[fl][p2] = 1
	id = fl*8 + p2;
	maxNum = max(id, maxNum)
	print(prefix,[fl,fr], suffix, [p1,p2])

def printAirplane(ap):
	for idx, line in enumerate(ap):
		print(idx,line)

printAirplane(airplane)
print(maxNum)
