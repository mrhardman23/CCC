textIn = input()

happyCount = 0
sadCount = 0

result = "none"

# Start of complicated

# My thought process
# I can loop through the string looking for indexes of happy faces
# and counting each happy face. Then, I have to update my index
# so that I don't double-count a happy face.
index = 0

while index != -1:
    index = textIn.find(":-)", index)

    if index != -1:
        happyCount += 1
        index += 1

index = 0

while index != -1:
    index = textIn.find(":-(", index)

    if index != -1:
        sadCount += 1
        index += 1

if happyCount > sadCount:
    result = "happy"
elif happyCount < sadCount:
    result = "sad"

print(result)