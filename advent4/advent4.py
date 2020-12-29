file = open("./data/advent4data.txt","r")
lines = file.readlines()

validPassports = 0
passports = []
tmpPassport = {}
for line in lines:
	if line == "\n":
		passports.append(tmpPassport)
		tmpPassport = {}
	else:
		fields = line[:-1].split(" ")
		for key in fields:
			passportKey, passportRes = key.split(":")
			tmpPassport[passportKey] = passportRes


def validHeight(s):
	suffix = s[-2:]
	try:
		height = int(s[:-2])
	except:
		return False		
	if suffix == "cm":
		if height >= 150 and height <= 193:
			return True
	elif suffix == "in":
		if height >= 59 and height <= 76:
			return True
	return False

def validHairColor(s):
	prefix = s[0]
	color = s[1:]
	valid = True;
	if prefix != "#":
		valid = False
	validChars = {"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"}
	for e in color:
		if e not in validChars:
			valid = False
	return valid 

def validEyeColor(s):
	valid = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
	if s in valid:
		return True
	else:
		return False

def validPassportId(s):
	valid = True
	if len(s) != 9:
		valid = False
	validChars = {"0","1","2","3","4","5","6","7","8","9"}
	for e in s:
		if e not in s:
			valid = False
	return valid

def validBirthYear(s):
	year = int(s)
	if year >= 1920 and year <= 2002:
		return True
	else: 
		return False

def validIssueYear(s):
	year = int(s)
	if year >= 2010 and year <= 2020:
		return True
	else:
		return False

def validExpYear(s):
	year = int(s)
	if year >= 2020 and year <= 2030:
		return True
	else:
		return False

criteria = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
for passport in passports:
	if passport.keys() >= criteria:
		#print(validExpYear(passport["eyr"]), validIssueYear(passport["iyr"]), validBirthYear(passport["byr"]))
		valid = validExpYear(passport["eyr"]) and validIssueYear(passport["iyr"]) and validBirthYear(passport["byr"]) and validPassportId(passport["pid"]) and validEyeColor(passport["ecl"]) and validHairColor(passport["hcl"]) and validHeight(passport["hgt"])
		#print(validEyeColor(passport["ecl"]), passport["ecl"])
		if valid:
			validPassports += 1
			print("valid", passport)
		else:
			print("not v", passport)	

print(validPassports)
