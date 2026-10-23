nilai = int(input("Masukkan nilai tes :"))
pengalaman = int(input("Masukkan pengalaman kerja (tahun):"))

if 80 <= nilai <= 100 :
    print("lolos ke tahap wawancara")
elif nilai >= 65 and pengalaman >= 2 :
    print("lolos bersyarat")
else :
    print("tidak lolos")