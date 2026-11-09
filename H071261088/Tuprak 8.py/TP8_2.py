#2. Penyaringan username
import re

def validasi_username(username):
    pola = r"^[A-Za-z][\w]{4,11}$"
    hasil = re.match(pola, username)
    return hasil is not None

daftar_valid = []
 
print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")

while True:
    print()
    username = input("Masukkan username: ").strip()
    if username.upper() == "SELESAI":
        break
    elif username in daftar_valid:
        print("sudah ada")
    elif validasi_username(username):
        daftar_valid.append(username)
        print("Username Tersedia.")
    
    else:
        print("Username tidak valid!")
    

print("\n=== Rekapitulasi ===")
if len(daftar_valid) == 0:
    print("Belum ada username yang valid.")
else:
    print("Username valid:")
    nomor = 1
    for nama in daftar_valid:
        print(f"{nomor}. {nama}")
        nomor += 1

print("\nJumlah username valid:", len(daftar_valid))
