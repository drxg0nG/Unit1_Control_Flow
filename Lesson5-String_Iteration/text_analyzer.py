text = input("Enter a text: ")

# Initialize counters
total_chars = len(text)
letter_count = 0
digit_count = 0
uppercase_count = 0
lowercase_count = 0

# Track first and last character
first_char = None
last_char = None

print(f"Analyzing: '{text}'")
print("=" * 30)

# Process each character
for char in text:
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        letter_count += 1
        if first_char is None:
            first_char = char
        last_char = char # Keep updating
    
    # Count uppercase
    if 'A' <= char <= 'Z':
        uppercase_count += 1
    
    # Count lowercase
    if 'a' <= char <= 'z':
        lowercase_count += 1
    
    # Count digits
    if '0' <= char <= '9':
        digit_count += 1

# Display the results
print(f"Total Characters: {total_chars}")
print(f"Letters: {letter_count}")
print(f"Digits: {digit_count}")
print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"First letter: {first_char}")
print(f"Last letter: {last_char}")
