DEBUG = True

def log(*args):
	if DEBUG:
		print(*args)

# returns (5, bagdescription), 0 = count, 1 = description
def cleanUpTargetBags(desc):
	if "no other" in desc:
		return None
	tmp = desc.strip().split(" ")[:-1]
	tuple = (tmp[0], "".join(tmp[1:]))
	return tuple

# creates adjlist for graph of bags
def createAdjList():
	adjList = {}
	file = open("./input.txt","r")
	lines = file.readlines()

	for line in lines:
		item, result = map(lambda x : x.strip(), line[:-2].split("contain"))
		result = list(map(cleanUpTargetBags, result.split(",")))
		sourceBagName = "".join(item.split(" ")[:-1])
		adjList[sourceBagName] = [] if result[0] == None else result

	return adjList

#  
def dfs(node, bagMap, target):
	nodePath = []

	def helper(node):
		nodePath.append(node)
		list = bagMap[node]
		res = []
	
		if node == target:
			return True 

		for numOfType, bagType in list:
			res.append(helper(bagType))
		
		if True in res:
			return True
		else:
			return False

	res = helper(node)
	
	log(res, nodePath)
	if res:
		return 1
	else:
		return 0

def dfs2(target, bagMap):
	memoBagCount = {}

	def helper(node):
		resLog = []
		res = 0

		list = bagMap[node]
		if len(list) == 0:
			return 0
		
		for numOfType, bagType in list:
			tmp = helper(bagType)
			resLog.append([int(numOfType), bagType, tmp])
			res += int(numOfType)
			res += (int(numOfType) * tmp)

		log(resLog)
		return res

	return helper(target)

def part1():
	target = "shinygold"
	bagMap = createAdjList()
	count = 0
	
	for item in bagMap:
		if item != target:
			count += dfs(item,bagMap, target)
			log("----")
	print(count)

def part2():
	bagMap = createAdjList()
	print(dfs2("shinygold", bagMap))

part2()
