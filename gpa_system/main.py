# main.py
import os
from students.student_manager import add_student
# Tambahkan import load_courses di sini
from courses.course_manager import add_course, load_courses
from grades.grade_manager import assign_grade
from reports.report_generator import generate_gpa_report

def main():
    # Membuat folder data otomatis jika belum ada
    if not os.path.exists('data'):
        os.makedirs('data')

    while True:
        print("\n=== SYSTEM AKADEMIK KONSOL (PANDAS ENABLED) ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Tambah Data Mata Kuliah")
        print("3. Input Nilai Semua Mata Kuliah per Mahasiswa")
        print("4. Jalankan Perhitungan & Ekspor Laporan GPA")
        print("5. Keluar")
        
        choice = input("Pilih Menu (1-5): ")
        
        if choice == '1':
            sid = input("ID Mahasiswa / NIM (Contoh: 20250040087): ")
            name = input("Nama Mahasiswa: ")
            group = input("Grup/Kelas (A/B): ")
            add_student(sid, name, group)
            
        elif choice == '2':
            code = input("Kode MK (Contoh: 25IF12006): ")
            name = input("Nama MK: ")
            sks = input("Jumlah SKS (Angka): ")
            if sks.isdigit():
                add_course(code, name, int(sks))
            else:
                print("❌ Input SKS gagal, harus angka.")
                
        elif choice == '3':
            # 1. Ambil daftar mata kuliah yang ada di database txt terlebih dahulu
            active_courses = load_courses()
            
            if not active_courses:
                print("❌ Gagal: Belum ada data mata kuliah. Silakan isi Menu 2 terlebih dahulu.")
                continue
                
            sid = input("Masukkan ID Mahasiswa / NIM: ")
            
            print(f"\n--- Menginput Nilai Untuk NIM: {sid} ---")
            # active_courses mengembalikan list of tuples: [(course_id, course_name, sks), ...]
            for course_id, course_name, sks in active_courses:
                # Loop akan bertanya berdasarkan Nama Mata Kuliah langsung
                score = input(f"Masukkan Nilai untuk {course_name} ({course_id}): ")
                
                # Panggil fungsi assign_grade bawaan kita
                success = assign_grade(sid, course_id, score)
                
                # Jika input gagal (misal salah ketik angka > 100), beri kesempatan mengulangi mata kuliah tersebut
                while not success:
                    print("⚠ Mohon ulangi input nilai dengan benar.")
                    score = input(f"Masukkan Nilai untuk {course_name} ({course_id}): ")
                    success = assign_grade(sid, course_id, score)
            
            print(f"\n✅ Berhasil menginput semua nilai untuk mahasiswa {sid}!")
            
        elif choice == '4':
            generate_gpa_report()
            
        elif choice == '5':
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("❌ Pilihan salah, ulangi.")

if __name__ == "__main__":
    main()