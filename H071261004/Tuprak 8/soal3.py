import re

jumlah_data = int(input("Masukkan jumlah nomor telepon: "))

data_sebelum = []
data_setelah = []
nomor_valid = []

for i in range(jumlah_data):
    nomor = input(f"Masukkan nomor telepon ke-{i + 1}: ")

    data_sebelum.append(nomor)

    nomor_bersih = re.sub(r"[\s-]", "", nomor)

    data_setelah.append(nomor_bersih)

    if re.fullmatch(r"\d{10,13}", nomor_bersih):
        nomor_valid.append(nomor_bersih)

print("\n=== DATA SEBELUM DIBERSIHKAN ===")
for nomor in data_sebelum:
    print(nomor)

print("\n=== DATA SETELAH DIBERSIHKAN ===")
for nomor in data_setelah:
    print(nomor)

print("\n=== DAFTAR NOMOR VALID ===")
for nomor in nomor_valid:
    print(nomor)

print("Jumlah nomor valid:", len(nomor_valid))