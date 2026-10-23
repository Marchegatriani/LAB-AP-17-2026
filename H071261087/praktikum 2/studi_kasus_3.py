# Studi Kasus 3

nilai = float(input("Masukkan nilai tes: "))
pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))

if 80 <= nilai <= 100:
    print("Lolos ke Tahap Wawancara")

elif 79 >= nilai >= 65 and pengalaman >= 2:
    print("Lolos Bersyarat")

else:
    print("Tidak Lolos")