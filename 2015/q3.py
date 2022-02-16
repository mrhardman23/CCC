'''
    Define an array of vowels to check letters against to see
    if a letter is a consonant or a vowel.
'''
vowels = ["a","e","i","o","u"]


'''
    isConsonant checks to see if a given vowel is a consonant or not.

    @param charToTest is the character that must be checked for whether
        it is a vowel or a consonant
    @return True or False depending on whether the letter is a consonant
        or a vowel, respectively.
'''
def isConsonant(charToTest):
    
    # Defines a variable that stores whether the letter is a consonant
    consonantCheck = True

    '''
        If I count all the instances of the charToTest in
        the vowels array and more than zero instances is
        found...
    '''
    if vowels.count(charToTest) != 0:
        '''
            Set the consonant check to represent that the letter is
            a vowel.
        '''
        consonantCheck = False

    # Return whether the letter is a consonant or a vowel.
    return consonantCheck


'''
    getClosestVowel will find the closest vowel in the alphabet based
    on a given consonant.

    @param charToUse is the consonant that will be the starting point for
        finding the closest vowel.
    @return a string that holds the closest vowel to a consonant.
'''
def getClosestVowel(charToUse):

    '''
        shift will store the amount of characters on either side
        of the consonant to check for the closest vowel.
    '''
    shift = 1

    # Define a variable that will store the closest vowel to the consonant.
    closestVowel = ""

    # While closestVowel does not have a value...
    while closestVowel == "":

        # For each vowel in the list of vowels...
        for v in vowels:

            '''
                If the character on the left side of the consonant
                that is currentIndex spaces away from the consonant
                is the same as the current vowel in the vowels list...
            '''
            if chr( ord(charToUse)-shift ) == v:
                # The closest vowel is the current vowel in the list.
                closestVowel = v

                '''
                    Otherwise, if the character on the right side is still
                    before z and the character on the right side of the 
                    consonant that is currentIndex spaces away from the 
                    consonant is the same as the current vowel in the 
                    vowels list...
                '''
            elif ord(charToUse)+shift <= ord("z") and chr( ord(charToUse)+shift ) == v:
                # The closest vowel is the current vowel in the list.
                closestVowel = v

        '''
            If a vowel has not been found, increase the currentIndex
            so that we can find a vowel in a spot farther away from
            the consonant.
        '''
        shift += 1

    # Once a vowel has been found, return the closest vowel.
    return closestVowel


'''
    getNextConsonant will find the next consonant after the given consonant.

    @param charToUse is the consonant that will act as the starting point.
    @return the next consonant from the alphabet.
'''
def getNextConsonant(charToUse):

    '''
        currentIndex will store how many positions to the right of the consonant we 
        are checking to find the next consonant.
    '''
    currentIndex = 1

    # Define a variable to store the next consonant in the alphabet.
    nextConsonant = ""

    # If the consonant to use is z...
    if charToUse == "z":
        # We will use z as the next consonant as well.
        nextConsonant = "z"
    # Otherwise, if the consonant is not z...
    else:
        # While the next consonant has not been found...
        while nextConsonant == "":

            '''
                Set the next consonant to the character that is found
                currentIndex spaces to the right of the consonant given.
            '''
            nextConsonant = chr( ord(charToUse)+currentIndex )

            # If next consonant can be found in the list of vowels...
            if vowels.count( nextConsonant ) != 0:
                # Increase currentIndex by 1
                currentIndex += 1

                # We have not found the next consonant, so empty the value.
                nextConsonant = ""
    
    # Once the next consonant has been found, return the next consonant found.
    return nextConsonant
            

# Get the original word from the user.
originalWord = input()

# Define a variable that will store the changed word.
newWord = ""

# For every letter in the original word...
for i in originalWord:

    # If the current letter is a consonant...
    if isConsonant(i):
        '''
            Set newWord to be a joining, without spaces, of what newWord currently is,
            the current consonant, the closest vowel to the current consonant, and the
            next consonant in the alphabet.
        '''
        newWord = "".join([newWord, i, getClosestVowel(i), getNextConsonant(i)])
    # If the current letter is not a consonant...
    else:
        '''
            Set newWord to be a joining, without spaces, of what newWord currently is
            and the current vowel.
        '''
        newWord = "".join([newWord,i])

# After the new word has been created, print the new word.
print(newWord)