# Kalkulator Belanja Sederhana
barang = ["Buku", "Pensil", "Penghapus"]
harga = [15000, 3000, 2000]
jumlah = []

print("=== Kalkulator Belanja ===")

# Input jumlah barang
for b in barang:
    j = int(input(f"Masukkan jumlah {b}: "))
    jumlah.append(j)

# Cetak tabel
print("\n-----------------------------------")
print(f"{'Barang':<10} {'Jumlah':<10} {'Subtotal':<10}")
print("-----------------------------------")

total = 0
for i in range(len(barang)):
    subtotal = harga[i] * jumlah[i]
    total += subtotal
    print(f"{barang[i]:<10} {jumlah[i]:<10} {subtotal:<10}")

print("-----------------------------------")
print(f"{'TOTAL':<10} {'':<10} {total:<10}")
print("-----------------------------------")
