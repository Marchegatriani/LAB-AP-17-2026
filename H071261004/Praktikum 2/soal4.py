tujuan = input("Masukkan tujuan(Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan waktu(Pagi/Malam): ")
pengunjung = input("Masukkan tipe pengunjung(Anak/Dewasa): ")

match tujuan : 
    case "Pantai": 
        if waktu == "Pagi" : 
            print("Paket rekomendasi : Paket A")
        elif waktu == "malam" and pengunjung == "Dewasa" : 
            print("Paket rekomendasi : Paket C")

        else:
            print("Paket rekomendasi : Tidak ada paket yang cocok")

    case "Pegunungan":
        if waktu == "Pagi" and pengunjung == "Dewasa" : 
            print("Paket rekomendasi: Paket B")
        elif waktu == "malam" and pengunjung == "Dewasa" : 
             print("Paket rekomendasi : Paket C")
        else:
            print("Paket rekomendasi: Tidak ada paket yang cocok")

    case "Kota" :
        if waktu == "Malam" : 
            print("Paket rekomendasi: Paket C ")
        else:
            print("Paket rekomendasi: tidak ada paket yang cocok")

    case _:
         print("Paket rekomendasi: tidak ada paket yang cocok")

             