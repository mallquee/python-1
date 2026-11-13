## --- Tugas 1: Tuple dan Set ---

# a. tuples mahasiswa
mahasiswa = ("Lala", "123456789", "Teknologi Informasi")
print(mahasiswa)

# b. mengakses data dengan index
print(mahasiswa[1])
print(mahasiswa[2])

# c. tidak bisa dilakukan
# mahasiswa[2] = "Teknologi Informasi"

# d. sets (himpunan)
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)


## --- Tugas 2: Manipulasi Dictionary ---

# a. membuat dictionary
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}
print(data_mahasiswa)

# b. mengupdate data
data_mahasiswa["prodi"] = "Sastra Mesin"
print(data_mahasiswa)

# akan ditambah jika tidak ada
data_mahasiswa.update({"angkatan": 2026})
print(data_mahasiswa)

# c. menghapus data
del data_mahasiswa["nim"]
print(data_mahasiswa)


## --- Tugas 3: Looping Dictionary ---

# a. dictionary keranjang
keranjang = {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}

# b. looping dengan items()
for key, value in keranjang.items():
    print(f"Harga {key}: Rp {value}")

# c. total belanja
total = 0
for value in keranjang.values():
    total += value
print(f"Total belanja: Rp {total}")