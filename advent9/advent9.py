DEBUG = False

file = open("./input.txt","r")
lines = map(lambda x: int(x), file.readlines())


def log(*arr):
	if DEBUG:
		print(*arr)	

def twoSumPossible(arr, target):
	res = set()
	for num in arr:
		if num in res:
			return True
		res.add(target-num)
		
	return False

preamble = 25
stack = []
exploitNumber = None
totalStack = []

for line in lines:
	lineVal = line
	totalStack.append(lineVal)
	if len(stack) < preamble:
		stack.append(lineVal)
	else:
		twoSumPossibleRes = twoSumPossible(stack,lineVal)
		if twoSumPossibleRes == False:
			log(lineVal, stack)
			exploitNumber = lineVal
			break
		stack.pop(0)
		stack.append(lineVal)
 

def findContinuousSum(arr, target):
	window = []
	sum = 0
	arrIndex = 0
	while arrIndex < len(arr):
		log(target,sum,window)
		val = arr[arrIndex]
		if sum == target:
			return window
		if sum < target:
			window.append(val)
			sum += val
			arrIndex += 1
		elif sum > target:
			sum -= window[0]
			window.pop(0)
	return None


res = findContinuousSum(totalStack, exploitNumber)
res.sort()
print(res[0]+res[-1])
