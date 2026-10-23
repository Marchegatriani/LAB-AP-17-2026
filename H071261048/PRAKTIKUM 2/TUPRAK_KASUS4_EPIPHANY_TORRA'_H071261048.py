tujuan = (input("masukkan tujuan (pantai/pegunungan/kota): "))
waktu = (input("masukkan waktu (pagi/malam): "))
tipe = (input("masukkan tipe pengunjung (anak/dewasa): "))

match tujuan:
    case "pantai":
        if waktu == "pagi":
            print("Paket rekomendasi: Paket A")
        elif waktu == "malam" and tipe == "dewasa":
            print("Paket rekomendasi: Paket C")
    case "pegunungan":
        if waktu == "pagi" and tipe == "dewasa":
             print("Paket rekomendasi: Paket B")
        elif waktu == "malam" and tipe == "dewasa":
            print("Paket rekomendasi: Paket C")
    case "kota":
        if waktu == "malam":
            print("Paket rekomendasi: Paket C")
        elif waktu == "malam" and tipe == "dewasa":
            print("Paket rekomendasi: Paket C")
    case _:
        print("Tidak ada paket yang cocok")
