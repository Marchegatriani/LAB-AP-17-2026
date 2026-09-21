presentase = int(input("Masukkan Presentase cabai: "))

if presentase < 0 or presentase > 100: 
    print("Input tidak valid")
elif presentase <= 10: 
    print("Level Aman")
elif presentase <= 40: 
    print("Level Sedang")
elif presentase <= 70:
    print("Level Pedas")
else:
    print("Level Ekstrem")
