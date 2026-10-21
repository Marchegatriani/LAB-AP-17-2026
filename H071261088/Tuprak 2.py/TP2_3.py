nilai = int(input("Masukkan nilai tes: "))

if 80 <= nilai <= 100:
    print("Lolos ke Tahap Wawancara")
elif 65 <= nilai <= 79:
    pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))
    if pengalaman >= 2:
        print("Lolos bersyarat")
    else:
        print("Tidak Lolos")
else:
    print("Input tidak valid")