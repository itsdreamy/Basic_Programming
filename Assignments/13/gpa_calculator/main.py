import os
from courses.course_manager import load_courses
from grades.grade_manager import assign_grade
from reports.report_generator import generate_gpa_report

def main():
    if not os.path.exists('data'):
        os.makedirs('data')

    while True:
        print("\n=== ACADEMIC SYSTEM CONSOLE (PANDAS ENABLED) ===")
        print("1. Input Student's Scores")
        print("2. Calculate & Export GPA Report")
        print("3. Leave")
        
        choice = input("Choose a Menu (1-3): ")
                
        if choice == '1':
            active_courses = load_courses()
            
            if not active_courses:
                print("Failed: Course is Not Available!")
                continue
                
            sid = input("Enter Student ID/NIM: ")
            
            print(f"\n--- Inputting Student ID Values: {sid} ---")
            for course_id, course_name, sks in active_courses:
                score = input(f"Masukkan Nilai untuk {course_name} ({course_id}): ")
                
                success = assign_grade(sid, course_id, score)
                
                while not success:
                    print("Please Repeat with The Right Value.")
                    score = input(f"Enter Score for {course_name} ({course_id}): ")
                    success = assign_grade(sid, course_id, score)
            
            print(f"\nSuccesfully Input Student's Score: {sid}!")
            
        elif choice == '2':
            generate_gpa_report()
            
        elif choice == '3':
            print("Program Stopped, Thank You!")
            break
        else:
            print("Wrong Choice. Please Do It Again!")

if __name__ == "__main__":
    main()