## --- LATIHAN BAGIAN 9: MANIPULASI DAN OPERASI LIST ---

# ==================== TUGAS 1 ====================
print("========== TUGAS 1 ==========")
kendaraan = ['motor', 'mobil', 'sepeda', 'bus']
print(f"kendaraan awal = {kendaraan}")

# a. Tambahkan 'truk' di akhir list
kendaraan.append('truk')
print(f"a. setelah append 'truk' = {kendaraan}")

# b. Sisipkan 'becak' pada index ke-1
kendaraan.insert(1, 'becak')
print(f"b. setelah insert 'becak' di index 1 = {kendaraan}")

# c. Hapus data yang berada paling belakang
kendaraan.pop()
print(f"c. setelah pop() = {kendaraan}")

# d. Ubah elemen 'sepeda' menjadi 'skuter'
index_sepeda = kendaraan.index('sepeda')
kendaraan[index_sepeda] = 'skuter'
print(f"d. setelah 'sepeda' diubah menjadi 'skuter' = {kendaraan}")

# e. Tampilkan jumlah total data di dalam list
jumlah_data = len(kendaraan)
print(f"e. jumlah total data = {jumlah_data}")


# ==================== TUGAS 2 ====================
print("\n========== TUGAS 2 ==========")
angka = [75, 80, 90, 75, 85, 100, 65]
print(f"angka awal = {angka}")

# a. Cari indeks skor 100
index_100 = angka.index(100)
print(f"a. skor 100 berada di indeks ke-{index_100}")

# b. Hitung banyaknya siswa yang mendapat skor 75
jumlah_75 = angka.count(75)
print(f"b. jumlah siswa dengan skor 75 = {jumlah_75}")

# c. Urutkan dari terkecil hingga terbesar
angka.sort()
print(f"c. setelah sort = {angka}")

# d. Balikkan urutan (terbesar ke terkecil)
angka.reverse()
print(f"d. setelah reverse = {angka}")


# ==================== TUGAS 3 ====================
print("\n========== TUGAS 3 ==========")
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]
print(f"menu utama sebelum digabung = {menu_utama}")

# Gabungkan menggunakan extend()
menu_utama.extend(menu_tambahan)
print(f"menu gabungan = {menu_utama}")


# ==================== TUGAS 4 ====================
print("\n========== TUGAS 4 ==========")
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# a. Tampilkan harga "Pensil" dengan indeks baris dan kolom
harga_pensil = data_barang[1][1]
print(f"a. harga Pensil = {harga_pensil}")

# b. Perulangan untuk menampilkan setiap barang
print("b. daftar barang:")
for barang in data_barang:
    print(f"Nama: {barang[0]}, Harga: {barang[1]}")