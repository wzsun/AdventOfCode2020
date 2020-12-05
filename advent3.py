file = open("./data/advent3data.txt","r")
lines = file.readlines()

def countTrees(left, right):
	map = []
	for line in lines:
	        tmp = ""
       		for i in range((len(lines)*right)/len(line[:-1])+1):
                	tmp += line[:-1]
        	map.append(tmp)
	
	pos = [0,0]
	treeCount = 0;
	while pos[0] < len(map)-1:
		pos = [pos[0]+left, pos[1]+right]
		if(map[pos[0]][pos[1]] == "#"):
			treeCount += 1
			map[pos[0]] = map[pos[0]][:pos[1]] + "X" + map[pos[0]][pos[1]+1:]
		else:
			map[pos[0]] = map[pos[0]][:pos[1]] + "O" + map[pos[0]][pos[1]+1:]
		#print(pos, map[pos[0]], len(map))
	return treeCount

#for line in map:
#	print(line)

ans = [];

ans.append(countTrees(1,1))
ans.append(countTrees(1,3))
ans.append(countTrees(1,5))
ans.append(countTrees(1,7))
ans.append(countTrees(2,1))

total = 1
for item in ans:
	total *= item;

print(ans)
print(total)
