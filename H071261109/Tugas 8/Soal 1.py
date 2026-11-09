import re


def validasi_nim(nim):
    return re.fullmatch(r"H071[0-9]{6}", nim) is not None


def validasi_email(email):
    return re.fullmatch(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9-]+\.)+[A-Za-z]{2,}", email) is not None


def validasi_telepon(telp):
    return re.fullmatch(r"(\+[0-9]{2})*[0-9]{10,13}", telp) is not None


def tampilkan_status(label, valid, pesan_error):
    print(f"{label} : {'Valid' if valid else pesan_error}")


def main():
    print("=== Validasi Data Mahasiswa ===\n")
    nim = input("Masukkan NIM      : ").strip()
    email = input("Masukkan Email    : ").strip()
    telp = input("Masukkan No. Telp : ").strip()

    nim_ok = validasi_nim(nim)
    email_ok = validasi_email(email)
    telp_ok = validasi_telepon(telp)

    print("\n--- Hasil Validasi ---")
    tampilkan_status("NIM         ", nim_ok, "Format NIM tidak valid!")
    tampilkan_status("Email       ", email_ok, "Format email tidak valid!")
    tampilkan_status("No. Telepon ", telp_ok, "Nomor telepon tidak valid!")

    if nim_ok and email_ok and telp_ok:
        print("\nData mahasiswa berhasil diverifikasi!")


if __name__ == "__main__":
    main()