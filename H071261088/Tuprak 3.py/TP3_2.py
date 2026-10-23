print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    try:
        baris = int(input("Masukkan jumlah baris: "))
        if baris <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue
        break
    except:
        print("Input baris harus berupa angka!")
        
while True:
    try:
        kursi = int(input("Masukkan jumlah kursi per baris: "))
        if kursi <= 0:
            print("Jumlah kursi tidak boleh 0")
            continue
        break
    except:
        print("Input hanya boleh angka")

for n in range(1, baris + 1):
    for m in range(1, kursi + 1):
        if m == 13:
            continue
        if n == 1 and m % 2 == 0:
            continue
        print(f"Baris {n}, Kursi {m}")