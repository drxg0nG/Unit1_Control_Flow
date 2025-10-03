# break statement in loops
# break - Exit loop immediately
# use cases:
'''
Stop when you find something
Exit early based on conditions
Get out of infinite loops
'''
count = 1
while count <= 10:
    print(count)
    if count == 5:
        break
    count += 1

while True:
    choice = input("Enter something: (q for quit)")
    if choice == 'q':
        print("You wanted to exit")
        break
    print(f"You entered {choice}")


# Find first divsor
n = 15
divisor = 2
