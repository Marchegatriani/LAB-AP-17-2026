import re

nama2 = []
pola_user = r"^[a-zA-Z]\w{4,11}$"

def validasi_user(nama, pola):
    return re.fullmatch(pola, nama) is not None

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.\n")
while True:
    username = input("Masukkan username: ")
    if username.strip().upper() == "SELESAI":
        break
    if not validasi_user(username, pola_user):
        print("Username tidak valid!\n")
    elif username in nama2:
        print("Username sudah dipakai!\n")
    else:
        print("Username tersedia.\n")
        nama2.append(username)

print("\n=== Username Valid ===")
for i, nama in enumerate(nama2, start=1):
    print(f"{i}. {nama}")
print(f"\nJumlah username valid: {len(nama2)}")