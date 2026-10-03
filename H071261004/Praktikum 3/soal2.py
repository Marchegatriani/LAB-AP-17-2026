print("--- Set Up Denah Kursi Bioskop ---")

while True:
    try:
        N = int(input("Masukkan jumlah Baris: "))
        if N <= 0:
            print("Jumlah baris harus lebih 0!")
            continue
        break
    except ValueError:
        print("Harus berupa angka!")

while True:
    try:
        M = int(input("Masukkan jumlah kursi per baris: "))
        if M <= 0:
            print("Jumlah kursi per baris harus lebih 0!")
            continue
        break
    except :
        print("Harus berupa angka!")

print("--- Daftar kursi tersedia ---")

for baris in range(1, N + 1):
    for kursi in range(1, M + 1):
        if kursi == 13:
            continue

        if baris == 1 and kursi % 2 == 0:
            continue

        print(f"Baris {baris} - Kursi {kursi}")
   