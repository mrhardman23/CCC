# Get month and day input from the user
month = int(input())
day = int(input())

# Set result to special so that if month is 2 and day 
# is 18, we don't have to change anything.
result = "Special"

# If month is less than 2...
if month < 2:
    # The month is January, which is before February.
    result = "Before"

# Otherwise, if month is greater than 2...
elif month > 2:
    # The month is March, April, etc., which is after February.
    result = "After"

# Otherwise, the month is February...
else:
    # If the day is less than 18...
    if day < 18:
        # The day is 1, 2, ..., 16, 17, which are before the 18th
        result = "Before"

    # Otherwise, if the day is greater than 18...
    elif day > 18:
        # The day is 19, 20, etc., which are after the 18th
        result = "After"

# Print the result, which will be changed if any of the
# above conditions were met or still special because
# month of 2 and day of 18 would be the only other option.
print(result)