age = int(input("Enter Your Age: "))
rating = input("Enter The Rating: ")
rate = ["G", "PG", "PG13", "R"]
G = int(0)
PG = int(6)
PG13 = int(13)
R = int(17)


if not age:
    print("ERROR: Enter a valid age")
else:
    if rating not in rate:
        print("ERROR: Enter a valid rating")
    else:
        print("Valid Inputs")
        if rating == "R":
            if age >= R:
                print("Approved! You can watch R rated films")
            else:
                print(f"Denied! You must be 17 years old to watch R rated films")
        elif rating == "PG13":
            if age >= PG13:
                print("Approved! You can watch PG-13 rated films")
            else:
                print(f"Denied! You must be 13 years old to watch PG-13 rated films")
        elif rating == "PG":
            if age >= PG:
                print("Approved! You can watch PG rated films")
            else:
                print(f"Denied! You must be 6 years old to watch PG rated films")
        elif rating == "G":
            if age >= G:
                print("Approved! You can watch G rated films")
            else:
                print(f"Denied! You must be 0 years old to watch G rated films")
        else:
            print("You haven't been born yet")

