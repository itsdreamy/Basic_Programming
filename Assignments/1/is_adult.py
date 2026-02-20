age = int( input("How old are you? "))

if age < 17 and age > 0:
    print("You're a minor!")
#The current oldest living person is Tomiko Itooka of Japan, who is 116 years old.
elif age >= 17 and age <= 120: 
    print("Sadly, u r an adult, deal with it!")
else:
    print("Invalid age!")