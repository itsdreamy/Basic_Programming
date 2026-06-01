text = input("Enter a sentence/word: ")
vowels = ['a', 'i', 'u', 'e', 'o']
count_vowels = 0
total_char = 0
count_consonant = 0

for i in text:
    if i != " ":
        total_char += 1
    if i in vowels:
        count_vowels += 1
    elif i not in vowels and i != " ":
        count_consonant += 1

print(f"text: {text}")
print(f"vowels: {count_vowels}")
print(f"consonants: {count_consonant}")
print(f"total character: {total_char}")
