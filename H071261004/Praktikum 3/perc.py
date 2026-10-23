baris = int(input("Masukkan jumlah baris: "))



for a in range(1, baris + 1):

    for b in range(baris - a):
        print(" ", end="")

    for b in range(2 * a - 1):
        print("*", end="")

    print()

    