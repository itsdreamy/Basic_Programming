score = float( input("Enter your score: "))

if score >= 85 and score <= 100:
    print(f"Your grade is A")
elif score >= 70 and score <= 100:
    print(f"Your grade is B")
elif score >= 60 and score <= 100:
    print(f"Your grade is C")
elif score < 60 and score >= 0:
    print(f"Your grade is D")
else:
    print(f"Invalid score")