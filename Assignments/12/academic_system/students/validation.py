def validate_student_id(student_id):
    if len(student_id) == 11 and student_id.isdigit():
        return True 
    else:
        return False


def validate_score(score):
    if score < 0 or score > 100:
        return "Invalid Score!"
    else:
        return score