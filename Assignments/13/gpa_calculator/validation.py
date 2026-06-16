def validate_score(score):
    """Check if the score is safe for conversion and in between 0-100.
    Return True if valid, False if invalid"""
    try:
        score_num = float(score)
        return 0 <= score_num <= 100
    except (ValueError, TypeError):
        return False
    
def validate_student_id(student_id):
    student_id = student_id.strip()
    return len(student_id) == 11 and student_id.isdigit()