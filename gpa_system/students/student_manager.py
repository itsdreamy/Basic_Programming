# students/student_manager.py
import os
from students.validation import validate_student_id

FILE_PATH = os.path.join("data", "students.txt")

def add_student(student_id, name, group):
    """
    Append student details ke data/students.txt dengan Group.
    Format: StudentID,StudentName,Group
    """
    if not validate_student_id(student_id):
        print("Invalid Student ID!")
        return False
    
    # Bersihkan input dari spasi yang tidak disengaja
    student_id = student_id.strip()
    name = name.strip()
    group = group.strip()

    # Cek apakah file baru/kosong untuk menulis header Pandas
    file_exists = os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0
    
    with open(FILE_PATH, "a") as f:
        if not file_exists:
            # Tulis header tanpa spasi agar klop dengan pd.read_csv()
            f.write("StudentID,StudentName,Group\n")
        # Letakkan \n di AKHIR baris
        f.write(f"{student_id},{name},{group}\n")
        
    print("Student Added Successfully!")
    return True

        
def load_students(as_dict=False):
    """
    Baca semua student dari data/students.txt
    Return list of tuples atau dictionary data mahasiswa
    """
    students = []
    try:
        with open(FILE_PATH, "r") as f:
            lines = f.readlines()
            if not lines:
                return {} if as_dict else []
                
            # Skip baris pertama (index 0) karena itu adalah Header Pandas
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
        # Mengembalikan dict dengan format {id: {'name': name, 'group': group}}
        return {sid: {'name': name, 'group': grp} for sid, name, grp in students}
        
    return students