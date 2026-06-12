# reports/report_generator.py
import pandas as pd
import os

def calculate_grade_point(score):
    """Mengubah nilai mentah (0-100) ke skala bobot 4.0"""
    if score >= 85: return 4.0
    elif score >= 75: return 3.0
    elif score >= 60: return 2.0
    elif score >= 50: return 1.0
    else: return 0.0

def generate_gpa_report():
    students_file = os.path.join('data', 'students.txt')
    courses_file = os.path.join('data', 'courses.txt')
    grades_file = os.path.join('data', 'grades.txt')

    if not (os.path.exists(students_file) and os.path.exists(courses_file) and os.path.exists(grades_file)):
        print("Gagal: File data di folder 'data/' belum lengkap.")
        return

    # Read data directly using Pandas
    df_students = pd.read_csv(students_file)
    df_courses = pd.read_csv(courses_file)
    df_scores = pd.read_csv(grades_file)

    if df_scores.empty:
        print("⚠ Data nilai masih kosong.")
        return

    # Clean header whitespaces just in case
    df_students.columns = df_students.columns.str.strip()
    df_courses.columns = df_courses.columns.str.strip()
    df_scores.columns = df_scores.columns.str.strip()

    try:
        # 1. Join Tables smoothly
        df_merged = pd.merge(df_scores, df_students, on='StudentID')
        df_merged = pd.merge(df_merged, df_courses, on='SubjectCode')

        # 2. Transform numerical score to GPA scale
        df_merged['GradePoint'] = df_merged['Score'].apply(calculate_grade_point)
        df_merged['TotalPoints'] = df_merged['GradePoint'] * df_merged['SKS']

        # 3. Aggregate data per student
        df_gpa = df_merged.groupby(['StudentID', 'StudentName']).agg(
            Total_SKS=('SKS', 'sum'),
            Sum_Points=('TotalPoints', 'sum')
        ).reset_index()

        # Calculate final GPA
        df_gpa['GPA'] = (df_gpa['Sum_Points'] / df_gpa['Total_SKS']).round(2)
        final_gpa_report = df_gpa[['StudentID', 'StudentName', 'Total_SKS', 'GPA']]

        # 4. Display terminal interface
        print("\n" + "="*20 + " GPA REPORT (PANDAS) " + "="*20)
        print(final_gpa_report.to_string(index=False))
        print("="*61)
        
        class_average_gpa = final_gpa_report['GPA'].mean()
        print(f"Rata-rata GPA Kelas: {class_average_gpa:.2f}\n")

        # 5. Export seamlessly to multi-sheet Excel Workbook
        output_filename = 'Data_Akademik_Final.xlsx'
        with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:
            df_courses.to_excel(writer, sheet_name='Subjects', index=False)
            df_students.to_excel(writer, sheet_name='Students', index=False)
            df_scores.to_excel(writer, sheet_name='RawScores', index=False)
            final_gpa_report.to_excel(writer, sheet_name='GPA_Report', index=False)
            
        print(f"💾 File Excel sukses dibuat: '{output_filename}' dengan sheet [GPA_Report]!")

    except KeyError as e:
        print(f"Column Error: Missing expected column key {e}")
        print("Pastikan header file teks di folder data/ menggunakan nama: StudentID, SubjectCode, Score, StudentName, SKS")