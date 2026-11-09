import re

def validasi_username(username):
    pola = r"[A-Za-z][A-Za-z0-9_*&%$#@]{4,11}"
    return re.fullmatch(pola, username) is not None


daftar_username = []

while True:
    username = input("Masukkan username (SELESAI untuk berhenti): ")

    if username == "SELESAI":
        break

    if validasi_username(username):
        print("Username tersedia.")
        daftar_username.append(username)
    else:
        print("Username tidak valid!")

print("\n=== DAFTAR USERNAME VALID ===")

if daftar_username:
    for username in daftar_username:
        print(username)
else:
    print("Tidak ada username valid.")

print("Jumlah username yang valid:", len(daftar_username))