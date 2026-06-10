from students.student_manager import add_student, load_students
from courses.course_manager import add_course, load_courses
from grades.grade_manager import assign_grade, load_grades
from reports.report_generator import generate_student_report

def main():
    while True:
        print("\n=== Academic System Menu ===")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Assign Grade")
        print("4. Generate Student Report")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            student_id = input("Enter Student ID (11 digits): ")
            name = input("Enter Student Name: ")
            add_student(student_id, name)

        elif choice == "2":
            course_id = input("Enter Course ID: ")
            course_name = input("Enter Course Name: ")
            add_course(course_id, course_name)

        elif choice == "3":
            student_id = input("Enter Student ID: ")
            course_id = input("Enter Course ID: ")
            try:
                score = int(input("Enter Score (0-100): "))
            except ValueError:
                print("Invalid score input!")
                continue
            assign_grade(student_id, course_id, score)

        elif choice == "4":
            student_id = input("Enter Student ID: ")
            generate_student_report(student_id)

        elif choice == "5":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
