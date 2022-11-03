# Emanuel Ramos
#
# 11/1/2022
#
# Description: prints a list of numbers from 1 to 50 and prints Divisible by 3 for all numbers
# divisible by 3 as well as printing Divisible by 5 for any number divisible by 5.
#

for numbers in range(1, 51):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("Divisible by both")

    elif numbers % 5 == 0:
        print("Divisible by 5")

    elif numbers % 3 == 0:
        print("Divisible by 3")

    else:
        print(numbers)
