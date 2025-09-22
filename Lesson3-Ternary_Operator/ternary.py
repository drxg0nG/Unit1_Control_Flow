# JS Ternary
'''
let status = age >= 18 ? "adult" : "minor"
let message = score >= 90 ? "Excellent" : "Keep Trying"
'''

# Python Ternary
age = 15
status = "adult" if age >= 18 else "minor"
score = 75
message = "Excellent" if score >= 90 else "Keept Trying!"

# Examples
password = "mypass123"
strength = "Strong" if len(password) >= 8 else "Weak"
print(f"Password: {password}")
print(f"Strength: {strength}")

# Combining Ternary + Chaining
category = ("Child" if 0 <= age <= 12 else
            "Teen" if 13 <= age <= 17 else
            "Adult" if 18 <= age <= 64 else
            "Senior"
            )

score = 89
grade = ("A" if 100 >= score >= 90 else
         "B" if 89 >= score >= 80 else
         "C" if 79 >= score >= 70 else
         "F"
        )
