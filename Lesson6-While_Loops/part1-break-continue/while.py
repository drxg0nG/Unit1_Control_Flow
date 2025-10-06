# Syntax
'''
while condition:
    code block
    increment / decrement variable
'''

# num = 5
# while num > 0:
#     print(num)
#     num -= 1

num = 1
sum = 0
# while num <= 10:
#     sum = sum + num
#     num += 1
# print(f"Sum of #'s 1-10 = {sum}")

while num <= 10:
    sum = sum + num
    if num < 10:
        print(num, end = " + ")
    else:
        print(num, end = " = ")
    num += 1
print(f"{sum}")
# print(f"{sum}")

# Sum of digits
# Take a user input as int, and sum of the digits in it
# number_input = input("Enter a number: ")
sum = 0
# for char in number_input:
#     # print(f"{char} {type(char)}")
#     number = int(char)
#     sum += number
# print(sum)

# i = 0
# while i < len(number_input):
#     sum += int(number_input[i])
#     i += 1
# print(f"Total: {sum}")


# Algorithm - sum of digits (as ints)
number_input = int(input("Enter a number: "))
number = number_input
sum = 0
while number > 0:
    digit = number % 10 # Get last digit
    sum += digit # Add to sum
    number = number // 10 # Removing last digit

print(f"The sum of digits {number_input}: {sum}")


# Algorithm - count digits (as ints)
# number_input = int(input("Enter a number: "))
number = 54321
count = 0
while number > 0:
    count += 1
    number = number // 10
print(f"{count}")