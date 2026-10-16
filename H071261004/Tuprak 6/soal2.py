def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()

    if nama:
        if nama in kandidat_set:
            print(f"'{nama}' sudah terdaftar!")
        else:
            kandidat_set.add(nama)
            print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")

    return kandidat_set


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih = nama_pemilih.strip().lower()
    pilihan = pilihan.strip().capitalize()

    if pemilih in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")

    elif pilihan not in kandidat_set:
        print("Kandidat tidak ditemukan! Suara tidak dicatat.")

    else:
        rekap_suara[pemilih] = pilihan
        print(
            f"Suara '{nama_pemilih}' untuk '{pilihan}' "
            "berhasil dicatat!"
        )

    return rekap_suara


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for nama in kandidat_set:
        perolehan[nama] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("\n========================================")
    print("   HASIL PEMILIHAN KETUA KELAS")
    print("========================================")

    for nama, suara in sorted(perolehan.items()):
        print(f"  {nama}: {suara} suara")

    if not perolehan:
        print("Belum ada kandidat.")
        return

    tertinggi = max(perolehan.values())

    pemenang = [
        nama for nama, suara in perolehan.items()
        if suara == tertinggi
    ]

    print("\nTotal suara masuk:", sum(perolehan.values()))

    if len(pemenang) > 1:
        print("Hasil SERI antara:", ", ".join(sorted(pemenang)))
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(
            f"PEMENANG: {pemenang[0]} "
            f"dengan {tertinggi} suara!"
        )

    print("========================================")


# PROGRAM UTAMA

kandidat_set = set()
rekap_suara = {}

print("========================================")
print("   SISTEM PEMILIHAN KETUA KELAS")
print("========================================")

# FASE PENDAFTARAN KANDIDAT

print("\n--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")

    if nama.strip() == "":
        break

    daftar_kandidat(kandidat_set, nama)

if len(kandidat_set) < 2:
    print("Kandidat harus berjumlah minimal 2 orang.")
else:
    print("\nKandidat terdaftar:", sorted(kandidat_set))

    # FASE PEMUNGUTAN SUARA

    print("\n--- FASE PEMUNGUTAN SUARA ---")

    while True:
        nama_pemilih = input(
            "\nNama pemilih (kosongkan untuk selesai): "
        )

        if nama_pemilih.strip() == "":
            break

        print("Kandidat yang tersedia:", sorted(kandidat_set))
        pilihan = input("Pilih kandidat: ")

        berikan_suara(
            rekap_suara,
            kandidat_set,
            nama_pemilih,
            pilihan
        )

    # MENAMPILKAN HASIL

    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)