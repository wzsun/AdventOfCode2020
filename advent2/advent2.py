file = open("./data/advent2data.txt","r")
lines = file.readlines()
globalCounter = 0

# PART ONE
def checkValidPassword(letter, min, max, s):
	count = 0;
	for letterInString in s:
		if(letter == letterInString):
			count += 1
	if(count <= max and count >= min):
		return True
	else:
		return False 

# PART TWO
def checkValidPasswordPart2(letter, i1, i2, s):
	if((s[i1] == letter and s[i2] != letter) or (s[i1] != letter and s[i2] == letter)):
		return True
	else:
		return False

for line in lines:
	maxmin, letter, s = line.split(" ")
	min, max = maxmin.split("-")
	min = int(min)
	max = int(max)
	letter = letter[0]
	if(checkValidPasswordPart2(letter, min-1, max-1, s)):
		globalCounter += 1


print(globalCounter)


