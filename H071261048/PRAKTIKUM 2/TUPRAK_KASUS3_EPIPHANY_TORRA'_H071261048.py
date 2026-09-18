nilai = int(input("Masukkan nilai tes: "))
if nilai >= 80:
    print ("Lolos ke tahap wawancara")
elif nilai < 80:
    pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))
    if nilai >= 65 and pengalaman >= 2:
        print("lolos bersyarat")
    else:
        print("tidak lolos")