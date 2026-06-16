import os

FILE_PATH = os.path.join("data", "students.txt")

def load_students(as_dict = False):
    """Read all data from student.txt
    Return list of tuples or dictionary student data"""
    students = []
    try:
        with open(FILE_PATH, "r") as f:
            lines = f.readlines()
            if not lines:
                return {} if as_dict else[]
            for line in lines[1:]:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 3:
                        student_id, name, group = parts
                        students.append((student_id, name, group))
    except FileNotFoundError:
        print("No student data found.")
        return {} if as_dict else []
    
    if as_dict:
        return{sid: {'name': name, 'group': grp} for sid, name, grp in students}
    
    return students