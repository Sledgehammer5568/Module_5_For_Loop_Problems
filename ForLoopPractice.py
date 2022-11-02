# This prints certain elements of the list "colors"
colors = ["red", "blue", "green"]
print(colors[0])  # printing different values here changes the element printed
# 0 = first, 1 = second, 2 = third, etc.

# this prints out the whole list of elements in the variable "colors" on its own line
for color in colors:
    print(color)

# this also prints all the elements of the list on its own line
for i in colors:
    print(i)

# this prints out all the numbers within the range on their own line
for number in range(1, 11):  # you must add 1 because the range stops 1 before the second number
    # to print the word number you can make the variable number = "number"
    print(number)  # <-- or you can change the number variable here to "number"

