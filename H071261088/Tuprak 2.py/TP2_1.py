persentase = int(input("Masukkan persentase cabai: "))

if 70 < persentase <= 100:
    print("Level Ekstrem")
elif 41 <= persentase <= 70:
    print("Level Pedas")
elif 11 <= persentase <= 40:
    print("Level Sedang")
elif 0 <= persentase <= 10:
    print("Level Aman")
else:
    print("Persentase cabai tidak valid")