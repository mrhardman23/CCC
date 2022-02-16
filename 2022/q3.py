instructions = input()

instructionsList = []

lastPosition = 0
currentFind = 0

while currentFind != -1:

    if instructions.find("+", lastPosition) != -1 and instructions.find("+", lastPosition) < instructions.find("-", lastPosition):
        currentFind = instructions.find("+", lastPosition)

    else:
        currentFind = instructions.find("-", lastPosition)

    shift = 1

    while (currentFind + shift + 1) < len(instructions) and instructions[(currentFind + shift + 1)].isdigit():
        shift += 1

    if currentFind != -1 and (currentFind + shift + 2) < len(instructions):
        instructionsList.append( instructions[lastPosition:(currentFind + shift + 1)] )

        lastPosition = currentFind + shift + 1
    else:
        instructionsList.append( instructions[lastPosition:(len(instructions)+1)])

        currentFind = -1

for i in instructionsList:

    currentInstruction = []

    if i.find("+") != -1:
        currentInstruction = i.split("+")

        print( currentInstruction[0] + " tighten " + currentInstruction[1] )
    else:
        currentInstruction = i.split("-")

        print( currentInstruction[0] + " loosen " + currentInstruction[1] )