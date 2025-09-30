password = input("Enter a password: ")
symbols = "~`!@#$%^&*()_+-={\\}[]|:;\"'<,>.?/"

# Password Analysis
password_length = len(password)
uppercase_letter = 0
lowercase_letter = 0
digits = 0
special_char = 0
strength = 0

# # Booleans
# password_length_boolean = False
# uppercase_letter_boolean = False
# lowercase_letter_boolean = False
# digits_boolean = False
# special_char_boolean = False


# Data
for char in password:
    if 'A' <= char <= 'Z':
        uppercase_letter += 1
    elif 'a' <= char <= 'z':
        lowercase_letter += 1
    elif '0' <= char <= '9':
        digits += 1
    elif char in symbols:
        special_char += 1

# Print
print("Password Analysis")
print("=" * 20)
print(f"Password: {password}")
print()
print("CHARACTER COUNTS:")
print(f"Length: {password_length}")
print(f"Uppercase letters: {uppercase_letter}")
print(f"Lowercase letters: {lowercase_letter}")
print(f"Digits: {digits}")
print(f"Special characters: {special_char}")
print()
print("REQUIREMENTS CHECK:")

# Length
if password_length > 8:
    print("Length (8+ characters): PASSED")
    # password_length_boolean = True
    strength += 1
else:
    print("Length (8+ characters): FAILED")

# Uppercase
if uppercase_letter > 0:
    print("Uppercase letters: PASSED")
    # uppercase_letter_boolean = 
    strength += 1
else:
    print("Uppercase letters: FAILED")

# Lowercase
if lowercase_letter > 0:
    print("Uppercase letters: PASSED")
    # lowercase_letter_boolean = True
    strength += 1
else:
    print("Uppercase letters: FAILED")

# Digits
if digits > 0:
    print("Digits: PASSED")
    # digits_boolean = True
    strength += 1
else:
    print("Digits: FAILED")

# Special
if special_char > 0:
    print("Special characters: PASSED")
    # special_char_boolean = True
    strength += 1
else:
    print("Special characters: FAILED")

print()
print("SECURITY ISSUES:")

# Repeated character 3+ times
repeated = ""
for i in range(len(password) - 2):
    if password[i] == password[i+1] == password[i+2]:
        print(f"Found three '{password[i]}' in a row")
        repeated = False
        if strength > 1:
            strength = strength - 1
if repeated == "":
    print("No issues")
print()

# Strength
strength_value = ("Really Bad" if strength == 0 else
                  "Weak" if strength == 1 else
                  "Medium" if strength == 2 else
                  "Strong" if strength == 3 else
                  "Really Strong" if strength == 4 else
                  "Perfect"
                  )
print(f"FINAL RATING: {strength_value}")

# print(f"{password_length_boolean}")
# print(f"{uppercase_letter_boolean}")
# print(f"{lowercase_letter_boolean}")
# print(f"{digits_boolean}")
# print(f"{special_char_boolean}")

