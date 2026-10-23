jumlah = int(input("Masukkan jumlah baris segitiga: "))
for a in range(1, jumlah+1):
    for b in range(jumlah-a):
        print(' ', end='')
    for b in range(2*a-1):
        print("*", end="")
    print()