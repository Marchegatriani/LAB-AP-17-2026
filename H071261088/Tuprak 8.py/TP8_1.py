#1. Validasi Data Mahasiswa
import re

def validasi_nim(nim):
    pola = r"^H071\d{6}$"
    hasil = re.match(pola, nim)
    return hasil is not None

def validasi_email(email):
    pola = r"^[\w]+@([A-Za-z]+\.)+[A-Za-z]+$"
    hasil = re.match(pola, email)
    return hasil is not None

def validasi_telepon(telepon):
    pola = r"^[+|08][\d]{10,13}$"
    hasil = re.match(pola, telepon)
    return hasil is not None

def status_teks(hasil, pesan_error):
    if hasil:
        return "Valid"
    return pesan_error

print("=== Validasi Data Mahasiswa ===\n")
nim = input("Masukkan NIM \t: ").strip()
email = input("Masukkan Email \t: ").strip()
telepon = input("Masukkan No. Telp : ").strip()

nim_valid = validasi_nim(nim)
email_valid = validasi_email(email)
telepon_valid = validasi_telepon(telepon)

print()
print("--- Hasil Validasi ---")
print("NIM         :", status_teks(nim_valid, "Format NIM tidak valid!"))
print("Email       :", status_teks(email_valid, "Format email tidak valid!"))
print("No. Telepon :", status_teks(telepon_valid, "Nomor telepon tidak valid!"))
print()

if nim_valid and email_valid and telepon_valid:
    print("Data mahasiswa berhasil diverifikasi!")