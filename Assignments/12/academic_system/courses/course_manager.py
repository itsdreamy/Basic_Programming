def add_course(course_id, course_name):
    """
    Append course details ke data/courses.txt
    Format: course_id,course_name
    """
    with open("data/courses.txt", "a") as f:
        f.write(f"{course_id},{course_name}\n")
    print("Course added successfully!")
    return True


def load_courses():
    """
    Baca semua course dari data/courses.txt
    Return list of tuples [(course_id, course_name), ...]
    """
    courses = []
    try:
        with open("data/courses.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:  # skip baris kosong
                    course_id, course_name = line.split(",", 1)
                    courses.append((course_id, course_name))
    except FileNotFoundError:
        print("No course data found.")
    return courses
