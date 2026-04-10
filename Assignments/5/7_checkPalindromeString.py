user_input= input("Enter a word: ")

reverse_word = ""

for word in user_input:
    reverse_word = word + reverse_word

if user_input == reverse_word:
    print(f"{user_input} is palindrome")
else:
    print(f"{user_input} is not palindrome")