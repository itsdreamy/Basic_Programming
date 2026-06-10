from students.validation import validate_student_id

def add_student(student_id, name):
    if not validate_student_id(student_id):
        print("Invalid Student ID!")
        return False
    
    with open("data/students.txt", "a") as f:
            f.write(f"\n{student_id}, {name}")
            print("Student Added Successfully!")
            return True
        
def load_students(as_dict=False):
    students = []

    try:
        with open("data/students.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    student_id, name = line.split(",", 1)
                    students.append((student_id, name))
    except FileNotFoundError:
        print("No student data found.")
        return {} if as_dict else []

    if as_dict:
        return {sid: name for sid, name in students}
    return students
