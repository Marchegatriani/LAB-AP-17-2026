kursi = int(input("Masukkan maksimal kursi bus: "))
total_pendapatan = 0 

while kursi > 0:
    print(f"Sisa kursi : {kursi}")
    umur = input("Masukkan umur penumpang: ")

    try: 
        umur = int(umur)
    
    except ValueError: 
        print("Input harus berupa angka! ")
        continue

    if umur < 0: 
        print("Umur tidak valid")
        continue

    if umur <= 5: 
        kategori = "Balita"
        harga = 0

    elif umur <= 12:
        kategori = "Anak"
        harga = 50000

    else:
        kategori = "Dewasa"
        harga = 100000

    print(f"Kategori: {kategori} - Harga: Rp {harga:,}")

    kursi -= 1 
    total_pendapatan += harga 

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan:,} ")