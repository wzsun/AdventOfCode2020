file = open("./data/advent6data.txt","r")

lines = file.readlines()

count = 0;
groupToQuestion = {}
numberOfQuestions = {}
numberOfPeople = 0
for line in lines:
	if line == "\n":
		groupToQuestion[count] = {"people": numberOfPeople, "numberOfQuestions": numberOfQuestions}
		numberOfQuestions = {}
		count += 1
		numberOfPeople = 0
	else:	
		numberOfPeople += 1
		for question in line[:-1]:
			numberOfQuestions[question] = numberOfQuestions.get(question,0) + 1


total = 0
for group in groupToQuestion:
	people = groupToQuestion[group]["people"]
	numberOfQuestions = groupToQuestion[group]["numberOfQuestions"]
	for question in numberOfQuestions:
		if numberOfQuestions[question] == people:
			total += 1
print(total)
