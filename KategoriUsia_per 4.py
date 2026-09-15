# ELIF = else if statement

usia = input("Berapa usia anda: ")
usia = int(usia)

# if kondisi:
#       aksi true
# elif kondisi:
#       aksi true
# elif kondisi:
#       aksi true
# else:
#       aksi 

if usia > 0 and usia <= 12: #kondisi 1
    print("Usia anda masuk dalam kategori Anak Anak") #aksi true 1
elif usia <= 17: #kondisi 2
    print ("Usia anda masuk dalam kategori Remaja") #aksi true 2
elif usia <= 59: #kondisi 3
    print("Usia anda masuk dalam kategori Dewasa") #aksi true 3
elif usia >= 60: #kondisi 4
    print("Usia anda masuk dalam kategori Lansia") #aksi true 4
else:
    print("Usia tidak dikenal")
