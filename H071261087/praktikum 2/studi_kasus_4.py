# Studi Kasus 4

tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").capitalize()
waktu = input("Masukkan waktu (Pagi/Malam): ").capitalize()
tipe_pengunjung = input("Masukkan tipe penunjung (Anak/Dewasa): ").capitalize()

match tujuan:
    case "Pantai":
        if waktu == "Pagi" and tipe_pengunjung == "Anak" or tipe_pengunjung == "Dewasa": 
            print("Paket A")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "Pegunungan":
        if waktu == "Pagi" and tipe_pengunjung == "Dewasa":
            print("Paket B")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa" :
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "Kota":
        if waktu == "Malam":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case _:
        print("Tidak ada paket yang cocok")