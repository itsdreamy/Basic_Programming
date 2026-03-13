salary = float( input("Enter your employee's salary (dollars): "))
credit_score = float( input("Enter your credit score: "))
employement_duration = int( input("Enter your employement duration: "))

eligibility = True

if salary < 3000 :
    eligibility = False
elif credit_score < 650 :
    eligibility = False
elif employement_duration < 2:
    eligibility = False
else :
    eligibility = True

if eligibility == True :
    print("Congratulations, your loan application is accepted")
else :
    print("I am sorry, your loan application is rejected!")