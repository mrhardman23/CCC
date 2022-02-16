# Total # of players
numPlayers = int(input())

numStar = 0

result = ""

for i in range(numPlayers):
    numPoints = int(input())
    numFouls = int(input())

    totalPoints = numPoints * 5 - numFouls*3

    if totalPoints > 40:
        numStar += 1

result = str(numStar)

if numStar == numPlayers:
    result += "+"

print(result)