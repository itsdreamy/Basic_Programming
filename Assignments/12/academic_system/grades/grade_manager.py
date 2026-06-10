from students.validation import validate_student_id
from students.validation import validate_score  # kalau kamu mau pakai validasi skor

def assign_grade(student_id, course_id, score):
    """
    Append data to data/grades.txt
    Format: student_id,course_id,score
    """
    # Validasi ID dan skor (opsional)
    if not validate_student_id(student_id):
        print("Invalid Student ID!")
        return False
    if isinstance(score, str) or score < 0 or score > 100:
        print("Invalid Score!")
        return False

    with open("data/grades.txt", "a") as f:
        f.write(f"\n{student_id},{course_id},{score}")
    print("Grade assigned successfully!")
    return True


def load_grades():
    grades = []
    try:
        with open("data/grades.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 3:
                        student_id, course_id, score = parts
                        try:
                            grades.append((student_id, course_id, int(score)))
                        except ValueError:
                            print("Invalid score value:", score)
                    else:
                        print("Invalid grade line:", line)
    except FileNotFoundError:
        print("No grade data found.")
    return grades
