# Pyramid Pattern

# STEP-BY-STEP GUIDE:
# Row 0: 4 spaces, 1 star
# Row 1: 3 spaces, 3 star
# Row 2: 2 spaces, 5 star
# Row 3: 1 spaces, 7 star
# Row 4: 0 spaces, 9 star

rows = 5
cols = 9
spaces = 4
rest = 1
for i in range(rows):
    for j in range(cols):
        print(" " * spaces + "*" * rest)
        spaces -= 1
        rest += 2
        break