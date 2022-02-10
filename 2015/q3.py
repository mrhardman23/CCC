vowels = ['a','e','i','o','u']

def isConsonant(charToTest):
    consonantCheck = True

    for v in vowels:
        if charToTest == v:
            consonantCheck = False

    return consonantCheck

def getClosestVowel(charToUse):
    currentIndex = 1

    closestVowel = ''

    while closestVowel == '':
        

originalWord = input()

newWord = ""

for i in originalWord:

    if(isConsonant(originalWord[i])):
        newWord.__add__(originalWord[i])
        newWord.__add__(getClosestVowel(originalWord[i]))
