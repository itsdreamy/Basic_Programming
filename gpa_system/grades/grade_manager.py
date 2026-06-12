import os
from students.validation import validate_student_id

FILE_PATH = os.path.join("data", "grades.txt")

def assign_grade(student_id, course_id, score):
    """
    Append data to data/grades.txt
    Format: StudentID,SubjectCode,Score
    """
    if not validate_student_id(student_id):
        print("Invalid Student ID!")
        return False
        
    try:
        score_num = float(score)
        if score_num < 0 or score_num > 100:
            print("Invalid Score! Must be between 0 and 100.")
            return False
    except (ValueError, TypeError):
        print("Invalid Score! Must be a numeric value.")
        return False

    file_exists = os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0
    
    with open(FILE_PATH, "a") as f:
        if not file_exists:
            f.write("StudentID,SubjectCode,Score\n")
        f.write(f"{student_id},{course_id},{score_num}\n")
        
    print("Grade assigned successfully!")
    return True


def load_grades():
    """
    Baca semua grade dari data/grades.txt
    Return list of tuples [(student_id, course_id, score), ...]
    """
    grades = []
    try:
        with open(FILE_PATH, "r") as f:
            lines = f.readlines()
            if not lines:
                return grades
                
            for line in lines[1:]:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 3:
                        student_id, course_id, score = parts
                        try:
                            grades.append((student_id, course_id, float(score)))
                        except ValueError:
                            print("Invalid score value:", score)
                    else:
                        print("Invalid grade line:", line)
    except FileNotFoundError:
        print("No grade data found.")
    return grades