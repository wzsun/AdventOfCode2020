file = open("./puzzleinput.txt","r")
lines = file.readlines()

def runInstruction(op, val, currentIndex, acc):
	if op == "nop":
		return (currentIndex+1, acc)
	if op == "jmp":
		return (currentIndex + val, acc)
	if op == "acc": 
		return (currentIndex+1, acc+val)
	
	return (currentIndex,acc)

instructions = []
for line in lines:
	op, val = line[:-1].split(" ")
	val = int(val)
	instructions.append((op, val))


currentIndex = 0
visited = set()
acc = 0

def updateInstructionSet(origInstructions):
	indexPos = 0
	localOrigInstructions = origInstructions.copy()		

	def update():
		tmpInstructions = localOrigInstructions.copy()
		change = False
		nonlocal indexPos		
		
		while indexPos < len(localOrigInstructions):
			if localOrigInstructions[indexPos][0] == "nop":
				change = True
				tmpInstructions[indexPos] = ("jmp", tmpInstructions[indexPos][1])
			elif localOrigInstructions[indexPos][0] == "jmp":
				change = True
				tmpInstructions[indexPos] = ("nop", tmpInstructions[indexPos][1])
			
			if change:
				indexPos += 1
				return tmpInstructions
			else:
				indexPos += 1

		return None
	
	return update

getNextInstructionSet = updateInstructionSet(instructions)
while currentIndex < len(instructions):
	op, val = instructions[currentIndex]
	if currentIndex not in visited:
		visited.add(currentIndex)
		currentIndex, acc = runInstruction(op, val, currentIndex, acc)
	else:	
		if currentIndex == len(instructions) - 1:
			print("done", acc)
		else:
			# reset
			currentIndex = 0
			acc = 0
			visited = set()
			instructions = getNextInstructionSet()
			if instructions == None:
				print('something wrong')
				break

print(acc)
