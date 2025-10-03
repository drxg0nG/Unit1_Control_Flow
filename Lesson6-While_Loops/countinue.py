# The Continume Statement
'''
continue = Skip to next iteration!

Difference from break:
    - break -> Exit the loop completely
    - countinue -> Skip current iteration, keep looping
'''
# Example skip 3
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count) # 1, 2, _, 4, 5
