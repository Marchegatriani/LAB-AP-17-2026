import re

def validasi_nim(nim):
    return re.fullmatch(r"H071\d{6}", nim) is not None

def validasi_email(email):
    return re.fullmatch(
        r"[A-Za-z0-9._%+-] + @[A-Za-z0-9.-] + \.[A-Za-z]{2,}",
        email
    ) is not None

def validasi_telepon(telepon):
    return re.fullmatch(r"[._%+-]+\d{10,13}", telepon) is not None


nim = input("Masukkan NIM mahasiswa: ")
email = input("Masukkan email mahasiswa: ")
telepon = input("Masukkan nomor telepon: ")

if validasi_nim(nim):
    print("NIM valid.")
else:
    print("Format NIM tidak valid!")

if validasi_email(email):
    print("Email valid.")
else:
    print("Format email tidak valid!")

if validasi_telepon(telepon):
    print("Nomor telepon valid.")
else:
    print("Nomor telepon tidak valid!")

if (validasi_nim(nim) and
    validasi_email(email) and
    validasi_telepon(telepon)):
    print("Data mahasiswa berhasil diverifikasi!")