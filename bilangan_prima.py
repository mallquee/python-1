# latihan bilangan prima
print("Bilangan prima antara 1 - 100:")
for angka in range(2, 101):
    is_prima = True
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            is_prima = False
            break  # kontrol alur break, hentikan pengecekan begitu ketemu pembagi
    if is_prima:
        print(angka)