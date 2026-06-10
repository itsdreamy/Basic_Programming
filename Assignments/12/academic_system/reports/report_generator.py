from students.student_manager import load_students
from courses.course_manager import load_courses
from grades.grade_manager import load_grades

def generate_student_report(student_id):
    # Load semua data
    students = dict(load_students(as_dict=True))  # {id: name}
    courses = dict(load_courses())                # {id: name}
    grades = load_grades()                        # [(student_id, course_id, score), ...]

    # Cari student
    if student_id not in students:
        print("Student not found!")
        return

    student_name = students[student_id]
    print("="*40)
    print(f"Academic Transcript for {student_name} ({student_id})")
    print("="*40)

    # Ambil semua grade untuk student
    student_grades = [(cid, score) for sid, cid, score in grades if sid == student_id]

    if not student_grades:
        print("No grades found for this student.")
        return

    total_score = 0
    for course_id, score in student_grades:
        course_name = courses.get(course_id, "Unknown Course")
        print(f"{course_id} - {course_name}: {score}")
        total_score += score

    avg_score = total_score / len(student_grades)
    print("-"*40)
    print(f"Average Score: {avg_score:.2f}")
    print("="*40)
