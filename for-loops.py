# Three forms of range() function
# 1. range(stop)
for i in range(5): # 0, 1, 2, 3, 4
    print(i)

# 2. range(start, stop)
for i in range(3, 8): # 3, 4, 5, 6, 7
    print(i)

# 3. range(start, step, stop)
for i in range(2, 11, 2): # 2, 4, 6, 8, 10
    print(i)

# Counting Backwards
for i in range(10, 1, -2): # 10, 8, 6, 4, 2
    print(i)

# Countdown Timer
import time
for i in range(10, 0, -1):
    print(f"T-minus {i}")
    time.sleep(1)
print("Blast Off! 🚀")

# Multiplication Table
# Take user input for the number and print the table
# number x 1 = number
# number x 2 = number
# number x 3 = number
# number x 4 = number
# number x 5 = number
# number x 6 = number
# number x 7 = number
# number x 8 = number
# number x 9 = number
# number x 10 = number
input_number = int(input("Input number please (0-12): "))
if 0 < input_number < 13:
    for i in range(1, 13):
        print(f"{i:2d}: {(input_number * i):3d}")
else:
    print("Why you no listen. I tell you to put between 0 and 12")
