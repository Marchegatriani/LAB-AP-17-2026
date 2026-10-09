def deteksi_anomali_email(email, daftar_email):
    error = []
    jumlah_at = email.count('@')

    if jumlah_at != 1:
        error.append("Email harus mengandung tepat satu '@'.")

        return error

    posisi_at = email.find("@")
    local = email[:posisi_at]
    domain = email[posisi_at + 1:]

    if local == " " and domain == " ":
        error.append("Bagian sebelum @ (local) atau bagian setelah @ (domain) tidak boleh kosong.")

    if " " in email:
            error.append("Email tidak boleh mengandung spasi diposisi manapun.")

    if local != "":
        if local[0] == "." or local[-1] == ".":
                error.append("Bagian local tidak boleh diawali atau diakhiri dengan titik (.).")

        if ".." in local:
            error.append("Bagian local tidak boleh mengandung dua titik berturut-turut (..).")

    if domain != "":
        if "." not in domain:
            error.append("Bagian domain hwajib memiliki minimal satu titik (.).")  

        if ". ." in domain:
            error.append("Bagian domain tidak boleh mengandung titik berurutan (. .)")

        if domain[-1] == ".":
            error.append("Bagian domain tidak boleh diakhiri titik.")

    if not (domain.endswith(".com") or domain.endswith(".id") or domain.endswith(".ac.id")):
            error.append("Wajib berakhiran dengan .com, .id, ,ac.id")

    if email.lower() in daftar_email:
            error.append("Email duplikat")

    return error 

def cetak_daftar(daftar_email_valid, karakter_border):
    if len (daftar_email_valid) == 0:
        return

    email_terpanjang = daftar_email_valid[0]

    for email in daftar_email_valid:
        if len(email) > len(email_terpanjang):
            email_terpanjang = email 

    lebar = len(email_terpanjang) + 4
    print("\n" + karakter_border * lebar)

    for email in daftar_email_valid:
        padding = " " * (lebar - len(email) - 2)
        print(karakter_border + " " + email + padding + karakter_border)
    print(karakter_border * lebar)

daftar_email_valid = []

karakter_border = input("Masukkan border dengan karakter bebas:")

print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

while True:
    email = input("Masukkan email:")

    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(email, daftar_email_valid)

    if len(error) == 0:
        daftar_email_valid.append(email.lower())

        print(">> Email VALID")
    else:
        print("Email DITOLAK karena: ")

        for alasan in error:
            print("-", alasan)

print("--- Email Yang Valid ---")

cetak_daftar(daftar_email_valid, karakter_border)








    