text = "Hello World"
# for char in text:
#     if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char =="O" or char == "U":
#         print(f"{char} is a vowel")

vowel_count = 0
vowels = "aeiouAEIOU"
for char in text:
    if char in vowels:
        vowel_count += 1
print(f"Vowels in {text}: {vowel_count}")

text2 = "ABC123xyz"
for i in range(len(text2)):
    if "0" <= text2[i] <= "9":
        print(f"Digit at position {i}: {text2[i]}")

word = "Hello"
for i in range(len(word)):
    print(f"{word[i]} at index {i} and {word[-1-i]} at index {word[-1-i]}")