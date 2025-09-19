age = input("Enter Your Age: ")
rating = input("Enter The Rating: ")
rate = "G", "PG", "PG-13", "R"
G = 0
PG = 6
PG13 = 13
R = 17


if not age:
    print("ERROR: Enter a valid age")
else:
    int(age)
    if rating != rate:
        print("ERROR: Enter a valid rating")
    else:
        if age > G:
            print()
        elif age > PG:
            print()
        elif age > PG13:
            print()
        elif age > R:
            print()
        else:
            print()

