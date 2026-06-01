def is_passed(student_score, passing_score):
    if passing_score <= student_score:
        return True
    else: 
        return False
    
passing_score = int(input("Enter the passing grade: "))
student_score = int(input("Enter the student's grade: "))

result = is_passed(student_score, passing_score)

if result == True:
    print("Student passed!")
else:
    print("Student is not passed!")


# Scenario: A teacher wants to automatically identify students who score below the passing grade.

# Function Specifications:

# Create a function called is_passed with 2 parameters: student_score and passing_score.
# The function must check whether student_score is greater than or equal to passing_score.
# Required: Return a Boolean value: True if the student passes, and False otherwise.