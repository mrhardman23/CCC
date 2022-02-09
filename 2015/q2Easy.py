# Get text from the user
textIn = input()

# Count the number of :-) in the input from the user
happyCount = textIn.count(":-)")

# Count the number of :-( in the input from the user
sadCount = textIn.count(":-(")

# Set up result variable that will store what I print out
result = ""

# If there are no :-) AND no :-(...
if happyCount == 0 and sadCount == 0:
    # Result is none.
    result = "none"
# Otherwise, if the number of :-) is more than :-(...
elif happyCount > sadCount:
    # You are happy!
    result = "happy"
# Otherwise, if the number of :-) is less than :-(...
elif happyCount < sadCount:
    # You are sad...
    result = "sad"
# If the number of :-) is the same as :-(...
else:
    # You're in a class case of emotions...
    result = "unsure"

# Print the result
print(result)