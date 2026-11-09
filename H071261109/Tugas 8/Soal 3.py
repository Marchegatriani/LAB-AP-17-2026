import re


def bersihkan_nomor(nomor):
    return re.sub(r"[\s\-]", "", nomor)


def nomor_valid(nomor_bersih):
    return re.fullmatch(r"[0-9]{10,13}", nomor_bersih) is not None


def main():
    print("=== Pembersihan Data Nomor Telepon ===\n")

    while True:
        try:
            jumlah = int(input("Masukkan jumlah data: "))
            if jumlah > 0:
                break
            print("Jumlah harus lebih dari 0.")
        except ValueError:
            print("Input harus berupa angka.")

    sebelum = []
    sesudah = []
    nomor_valid_list = []

    print()
    for i in range(1, jumlah + 1):
        nomor = input(f"Nomor ke-{i}: ")
        bersih = bersihkan_nomor(nomor)
        sebelum.append(nomor)
        sesudah.append(bersih)
        if nomor_valid(bersih):
            nomor_valid_list.append(bersih)
        print()

    print("--- Hasil Pembersihan ---\n")
    for i in range(jumlah):
        status = "Valid" if nomor_valid(sesudah[i]) else "Tidak valid"
        print(f"Data {i + 1}:")
        print(f"Sebelum : {sebelum[i]}")
        print(f"Sesudah : {sesudah[i]}")
        print(f"Status  : {status}\n")

    print(f"Jumlah nomor valid: {len(nomor_valid_list)}")


if __name__ == "__main__":
    main()