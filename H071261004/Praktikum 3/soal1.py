print("--- Rekapitulasi Transaksi Dins Store ---")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi")

while True:
    jumlah = input("Masukkan Jumlah Item : ")

    try:
        jumlah = int(jumlah)

    except ValueError:
        print("Input harus berupa angka!")
        continue

    if jumlah == 0:
                print("Toko ditutup. Sesi rekap selesai.")
                break
    
    if jumlah < 0:
        print("Jumlah tidak boleh negatif")
        continue

    if jumlah > 100:
        print("Maksimal 100 item per sesi.")
        continue

    print(f"Transaksi {jumlah} item berhasil!")

    