import re


def validasi_username(username):
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{4,11}", username) is not None


def main():
    print("=== Registrasi Username ===")
    print("Ketik 'SELESAI' untuk mengakhiri.\n")

    username_valid = []

    while True:
        username = input("Masukkan username: ")
        if username.strip() == "SELESAI":
            break

        if validasi_username(username):
            print("Username tersedia.\n")
            username_valid.append(username)
        else:
            print("Username tidak valid!\n")

    print("\n=== Rekapitulasi ===")
    if username_valid:
        print("Username valid:")
        for i, nama in enumerate(username_valid, 1):
            print(f"{i}. {nama}")
            
    else:
        print("Tidak ada username yang valid.")
    print(f"\nJumlah username valid: {len(username_valid)}")


if __name__ == "__main__":
    main()