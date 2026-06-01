def calculate_score (uts = 0, uas = 0) :
    avg = (uts + uas) / 2
    print(f"Your uts score is {uts}")
    print(f"Your uas score is {uas}")
    print(f"Your average score is {avg}")
    if avg >= 85:
        print("Your grade is A")
    elif avg >= 70 and avg < 85:
        print("Your grade is B")
    elif avg >= 55 and avg < 70:
        print("Your grade is C")
    elif avg < 55 and avg >= 0 :
        print("Your grade is D")
    else :
        print("Invalid Score!")
    
calculate_score(80, 90)


