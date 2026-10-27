kandidat = set()
rekap_suara_nya = {}

def daftar_kandidat(kandidat_set, nama):
    if nama in kandidat_set:
        print(f"{nama} telah ada di dalam daftar!")
    else:
        kandidat_set.add(nama)

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    if nama_pemilih in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print(f"Tidak ada kandidat dengan nama '{pilihan}'")
    else:
        rekap_suara[nama_pemilih] = pilihan
        print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0
    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1
    return perolehan

def tampilkan_hasil(perolehan):
    tertinggi = max(perolehan.values())
    ada_berapa_pemilih = sum(perolehan.values())

    pemenang = [nama for nama, skor in perolehan.items() if skor == tertinggi]

    print()
    print("=================================")
    print("   HASIL PEMILIHAN KETUA KELAS")
    print("=================================")
    for nama, skor in perolehan.items():
        print(f"   {nama}: {skor} suara")
    print()
    print(f"Total suara masuk: {ada_berapa_pemilih}")

    if len(pemenang) > 1:
        print(f"Hasil SERI antara :{', '.join(pemenang)}, perlu pemilihan ulang")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")

print("==================================")
print("   SISTEM PEMILIHAN KETUA KELAS")
print("==================================")
while True:
    nama_kandidat = input("Masukkan nama kandidat (kosongkan untuk selesai): ").title ()
    if nama_kandidat == "":
        print()
        break
    daftar_kandidat(kandidat, nama_kandidat)
    print(f"'{nama_kandidat}' berhasil didaftarkan sebagai kandidat!")

if len(kandidat) < 2:
    print("Minimal ada 2 kandidat untuk melanjutkan")
else:
    print(f" Kandidat terdaftar: {kandidat}")
    print()
    print("--- FASE PEMUNGUTAN SUARA ---")
    while True:
        print()
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").title ()
        if nama_pemilih == "":
            break
        print(f"Kandidat yang tersedia: {kandidat}")
        pilih_kandidat = input("Pilih kandidat: ").title ()
        if pilih_kandidat == "":
            print("Nama kandidat tidak boleh kosong")
            continue
        berikan_suara(rekap_suara_nya, kandidat, nama_pemilih, pilih_kandidat)
    perolehan = hitung_suara(rekap_suara_nya, kandidat)
    tampilkan_hasil(perolehan)