user_input = input("Enter a sentence: ")
count_space = 0
count_word = 1

for index, i in enumerate(user_input, 1):
    if i == " ":
        count_space += 1
        count_word += 1

character_count = index - count_space
print(f'Total characters (without space) in "{user_input}" is {character_count}')
print(f'Total words in "{user_input}" is {count_word}')
