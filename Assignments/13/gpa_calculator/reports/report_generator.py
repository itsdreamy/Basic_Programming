import os
import pandas as pd

def calculate_grade_point(score):
    if score >= 85: return 4.0
    elif score >= 75: return 3.0
    elif score >= 60: return 2.0
    elif score >= 50: return 1.0
    else: return 0.0

def generate_gpa_report():
    students_file = os.path.join('data', 'students.txt')
    grades_file = os.path.join('data', 'grades.txt')
    courses_file = os.path.join('data', 'courses.txt')

    if not (os.path.exists(students_file) and os.path.exists(courses_file) and os.path.exists(grades_file)):
        print("Failes: File isn't complete yet!")
        return
    
    df_students = pd.read_csv(students_file)
    df_grades = pd.read_csv(grades_file)
    df_courses = pd.read_csv(courses_file)

    if df_grades.empty:
        print("Score is still empty.")
        return
    
    df_students.columns = df_students.columns.str.strip()
    df_grades.columns = df_grades.columns.str.strip()
    df_courses.columns =  df_courses.columns.str.strip()

    try:
        df_merged = pd.merge(df_grades, df_students, on='StudentID')
        df_merged = pd.merge(df_merged, df_courses, on='SubjectCode')

        df_merged['GradePoint'] = df_merged['Score'].apply(calculate_grade_point)
        df_merged['TotalPoints'] = df_merged['GradePoint'] * df_merged['SKS']

        df_gpa = df_merged.groupby(['StudentID', 'StudentName']).agg(
            Total_SKS = ('SKS', 'sum'),
            Sum_Points = ('TotalPoints', 'sum')
        ).reset_index()

        df_gpa['GPA'] = (df_gpa['Sum_Points'] / df_gpa['Total_SKS']).round(2)
        final_gpa_report = df_gpa[['StudentID', 'StudentName', 'Total_SKS', 'GPA']]

        print("\n" + "="*20 + " GPA REPORT (PANDAS) " + "="*20)
        print(final_gpa_report.to_string(index=False))
        print("="*61)

        class_avg_gpa = final_gpa_report['GPA'].mean()
        print(f"Rata-rata GPA Kelas: {class_avg_gpa:.2f}\n")

        output_filename = 'Data_Akademik_Final.xlsx'
        with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:
            df_courses.to_excel(writer, sheet_name='Subjects', index=False)
            df_grades.to_excel(writer, sheet_name='RawScores', index=False)
            df_students.to_excel(writer, sheet_name='Students', index=False)
            final_gpa_report.to_excel(writer, sheet_name='GPA_Report', index=False)

        print(f"File Successfully Created: '{output_filename}' with sheet [GPA_Report]!")

    except KeyError as e:
        print(f"Column Error: Missing expected column key {e}")
        print("Make sure header file in data/ using name: StudentID, SubjectCode, Score, StudentName, SKS")