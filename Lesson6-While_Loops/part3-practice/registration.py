while True:
    username = input("Enter a username: ")
    
    if len(username) < 3:
        print("Username too small")
        continue
    if len(username) > 15:
        print("Username too long")
        continue
    has_space = True
    for char in username:
        if char == " ":
            has_space = True
            print("Username can't have spaces")
            continue
    break

while True:
    password = input("Enter a password: ")
    has_uppercase = False
    has_digit = False
    if len(password) < 8:
        print("Password too small")
        continue
    for char in password:
        if 'A' <= char <= 'Z':
            has_uppercase = True
        if char.isdigit():
            has_digit = True


    if has_uppercase == False:
        print("No uppercase found")
        continue
    if has_digit == False:
        print("No digits found")
        continue
    break


while True:
    age = int(input("Enter your age: "))
    if age < 13:
        print("age must be greater than 12")
        continue
    if age > 120:
        print("age must be less than 121")
        continue
    break

while True:
    conformation = input("Enter y/n: ")
    if conformation == "n" or conformation == "no":
        print("you denied")
        continue
    if conformation == "y" or conformation == "yes":
        print("You accepted")
        break
