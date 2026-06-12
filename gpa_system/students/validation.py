# students/validation.py

def validate_student_id(student_id):
    """
    Validasi ID mahasiswa kustom (NIM).
    Memastikan panjangnya tepat 11 karakter dan semuanya berisi angka.
    """
    student_id = student_id.strip()
    return len(student_id) == 11 and student_id.isdigit()


def validate_score(score):
    """
    Memastikan score aman dikonversi ke angka dan berada di rentang 0-100.
    Mengembalikan True jika valid, False jika tidak valid.
    """
    try:
        # Ubah input text string dari console menjadi angka desimal/float
        score_num = float(score)
        return 0 <= score_num <= 100
    except (ValueError, TypeError):
        # Jika user memasukkan huruf atau karakter aneh, tangkap error-nya di sini
        return False