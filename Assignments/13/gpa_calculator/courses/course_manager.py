import os

FILE_PATH = os.path.join("data", "courses.txt")

def load_courses():
    """Read all course from data/courses.txt
    Return list of tuples"""

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