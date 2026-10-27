playlist = []
genre_unik = set()
genre_valid = {"pop": "Pop", "rock": "Rock", "jazz": "Jazz", "rnb": "RnB", "dangdut": "Dangdut"}


def format_durasi(detik):
    return f"{detik // 60}:{detik % 60}"


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!\n")


def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong.\n")
        return

    w_judul = max(len("Judul"), max(len(l[0]) for l in playlist))
    w_artis = max(len("Artis"), max(len(l[1]) for l in playlist))
    w_genre = max(len("Genre"), max(len(l[2]) for l in playlist))
    w_durasi = max(len("Durasi"), max(len(format_durasi(l[3])) for l in playlist))
    garis = "=" * (4 + w_judul + 2 + w_artis + 2 + w_genre + 2 + w_durasi)

    print(garis)
    print(f"{'No':<4}{'Judul':<{w_judul}}  {'Artis':<{w_artis}}  {'Genre':<{w_genre}}  {'Durasi':<{w_durasi}}")
    print(garis)
    for no, (judul, artis, genre, durasi) in enumerate(playlist, start=1):
        print(f"{no:<4}{judul:<{w_judul}}  {artis:<{w_artis}}  {genre:<{w_genre}}  {format_durasi(durasi):<{w_durasi}}")
    print(garis)

    total = sum(l[3] for l in playlist)
    print(f"Total durasi playlist: {total // 60} menit {total % 60} detik\n")


def filter_genre(playlist, genre_target):
    hasil = [l for l in playlist if l[2] == genre_target]
    if not hasil:
        print(f"Tidak ada lagu bergenre '{genre_target}'.\n")
        return
    print(f"Lagu bergenre '{genre_target}':")
    for no, (judul, artis, _, durasi) in enumerate(hasil, start=1):
        print(f"  {no}. {judul} - {artis} ({format_durasi(durasi)})")
    print()


def hapus_lagu(playlist, nomor):
    playlist.pop(nomor - 1)
    genre_unik.clear()
    for lagu in playlist:
        genre_unik.add(lagu[2])
    print(f"Lagu nomor {nomor} telah berhasil dihapus!")
    tampilkan_playlist(playlist)


def statistik_playlist(playlist, genre_set):
    if not playlist:
        print("Playlist masih kosong.\n")
        return

    distribusi = {}
    for lagu in playlist:
        genre = lagu[2]
        distribusi[genre] = distribusi.get(genre, 0) + 1

    terpanjang = max(playlist, key=lambda l: l[3])
    terpendek = min(playlist, key=lambda l: l[3])

    print("=" * 47)
    print("       STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 47)
    print(f"Total lagu        : {len(playlist)}")
    print(f"Jumlah genre unik : {len(genre_set)}")
    print(f"Daftar genre      : {', '.join(sorted(genre_set))}")
    print("\nDistribusi genre:")
    for genre, jumlah in distribusi.items():
        print(f"  {genre:<10}: {jumlah} lagu")
    print()
    print(f"Lagu terpanjang : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f"Lagu terpendek  : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("=" * 47 + "\n")


while True:
    print("===============================")
    print("   PLAYLIST MUSIK - PLAYTUNE")
    print("===============================")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ").strip()
    print()

    if pilihan == "1":
        judul = input("Judul lagu: ").strip().title()
        artis = input("Artis: ").strip().title()
        if not judul or not artis:
            print("Judul dan artis tidak boleh kosong.\n")
            continue
        genre_input = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip().lower()
        if genre_input not in genre_valid:
            print("Genre tidak valid.\n")
            continue
        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi <= 0:
                raise ValueError
        except ValueError:
            print("Durasi harus berupa angka positif.\n")
            continue
        tambah_lagu(playlist, genre_unik, judul, artis, genre_valid[genre_input], durasi)

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        if not genre_unik:
            print("Masukkan lagu terlebih dahulu.\n")
            continue
        print(f"Genre tersedia: {', '.join(sorted(genre_unik))}")
        target = input("Masukkan genre yang ingin difilter: ").strip().lower()
        filter_genre(playlist, genre_valid.get(target, target))

    elif pilihan == "4":
        if not playlist:
            print("Playlist masih kosong.\n")
            continue
        tampilkan_playlist(playlist)
        try:
            nomor = int(input("Masukkan nomor lagu yang ingin di hapus: "))
            hapus_lagu(playlist, nomor)
        except (ValueError, IndexError):
            print("Input yang anda masukkan tidak valid\n")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_unik)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid, masukkan angka 1-6.\n")