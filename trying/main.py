import pandas as pd

# 1. Tentukan nama file input dan output
file_txt = "data_siswa.txt"
file_excel = "data_siswa_exported.xlsx"

try:
    # 2. Membaca file .txt dengan separator koma (,)
    df = pd.read_csv(file_txt, sep=",")

    # Menampilkan data di console untuk memastikan data terbaca dengan benar
    print("Data berhasil dibaca dari file .txt:")
    print(df)
    print("-" * 40)

    # 3. Mengekspor DataFrame ke dalam format Excel
    # index=False digunakan agar nomor index bawaan pandas tidak ikut terbuat sebagai kolom baru
    df.to_excel(file_excel, index=False)

    print(f"Sukses! Data telah diexport ke file: '{file_excel}'")

except FileNotFoundError:
    print(
        f"Error: File '{file_txt}' tidak ditemukan. Pastikan posisinya satu folder dengan script ini."
    )
except Exception as e:
    print(f"Terjadi kesalahan: {e}")