numGroupsTogether = int(input())

groupsTogether = []

for i in range(numGroupsTogether):

    groupsTogether.append(input())


numPeopleCannot = int(input())

groupsCannot = []

for i in range(numPeopleCannot):

    groupsCannot.append(input())


numGroupsMade = int(input())

groupsMade = []

for i in range(numGroupsMade):

    groupsMade.append(input())


numViolations = 0

for i in groupsMade:
    for j in groupsTogether:
        
        individuals = j.split(" ")

        if (i.find(individuals[0]) != -1 and i.find(individuals[1]) == -1) or (i.find(individuals[0]) == -1 and i.find(individuals[1]) != -1):
            numViolations += 1

    for k in groupsCannot:
        
        individuals = k.split(" ")

        if i.find(individuals[0]) != -1 and i.find(individuals[1]) != -1:
            numViolations += 1

print(numViolations)