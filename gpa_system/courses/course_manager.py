import os

FILE_PATH = os.path.join("data", "courses.txt")

def add_course(course_id, course_name, sks):
    """
    Append course details ke data/courses.txt dengan SKS.
    Format: SubjectCode,SubjectName,SKS
    """
    file_exists = os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0
    
    with open(FILE_PATH, "a") as f:
        if not file_exists:
            f.write("SubjectCode,SubjectName,SKS\n")
        f.write(f"{course_id},{course_name},{sks}\n")
        
    print("Course added successfully!")
    return True


def load_courses():
    """
    Baca semua course dari data/courses.txt
    Return list of tuples [(course_id, course_name, sks), ...]
    """
    courses = []
    try:
        with open(FILE_PATH, "r") as f:
            lines = f.readlines()
            if not lines:
                return courses
                
            for line in lines[1:]:
                line = line.strip()
                if line:
                    course_id, course_name, sks = line.split(",")
                    courses.append((course_id, course_name, int(sks)))
    except FileNotFoundError:
        print("No course data found.")
    return courses