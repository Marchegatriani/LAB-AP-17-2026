inventaris = []


def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    ditemukan = False

    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            print(
                f"{buku['judul']} - {buku['penulis']} | "
                f"Rp{buku['harga']:g} | Stok: {buku['stok']}"
            )
            ditemukan = True

    if not ditemukan:
        print("Buku tidak ditemukan.")


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print("Gagal! Stok tidak boleh negatif.")
            else:
                buku["stok"] = stok_baru
                print(
                    f"Stok '{buku['judul']}' berubah. "
                    f"Stok sekarang: {buku['stok']}"
                )
            return

    print("Buku tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    jumlah_jenis = len(inventaris)
    total_stok = sum(buku["stok"] for buku in inventaris)
    total_aset = sum(
        buku["harga"] * buku["stok"] for buku in inventaris
    )

    print("\n========================================")
    print(" RINGKASAN INVENTARIS BOOKNEST")
    print("========================================")
    print("Jumlah jenis buku :", jumlah_jenis)
    print("Total seluruh stok:", total_stok)
    print(f"Total nilai aset  : Rp{total_aset:g}")

    if inventaris:
        termahal = max(inventaris, key=lambda buku: buku["harga"])
        print(
            f"Buku termahal     : {termahal['judul']} "
            f"(Rp{termahal['harga']:g})"
        )
    else:
        print("Buku termahal     : Belum ada buku")

    print("========================================")


while True:
    print("\n========================================")
    print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("========================================")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")

        try:
            harga = float(input("Harga: "))
            stok = int(input("Stok awal: "))

            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif.")
            else:
                tambah_buku(
                    inventaris, judul, penulis, harga, stok
                )

        except ValueError:
            print("Input salah! Harga harus angka dan stok harus bilangan bulat.")

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")

        try:
            jumlah = int(
                input("Jumlah perubahan (positif=tambah, negatif=kurang): ")
            )
            update_stok(inventaris, judul, jumlah)

        except ValueError:
            print("Jumlah perubahan harus berupa bilangan bulat.")

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-5.")