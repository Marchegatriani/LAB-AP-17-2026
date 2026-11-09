import re

# nomor = "0891-1937 1389"
# replace = ""
# hasil = re.sub(r'\D', '', nomor)
# print(hasil)------------------------> hanya sebagai pengingat

print("=== Pembersihan Data Nomor Telepon ===")

while True:
    try:
        jumlahdata = int(input("Masukkan jumlah data : "))
        if jumlahdata <= 0:
            print("Jumlah data harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input harus berupa angka!")

nomorasli = []
for x in range(1, jumlahdata + 1):
    nomor = input(f"Nomor ke-{x}: ")
    nomorasli.append(nomor)

nomor2 = []
nomor3 = []

for x in nomorasli:
    bersih = re.sub(r'[ -]', '', x)
    nomor2.append(bersih)

    if re.fullmatch(r'\d{10,13}', bersih):
        nomor3.append(bersih)

print("\n--- Hasil Pembersihan ---")

for i in range(jumlahdata):
    status = "Valid" if nomor2[i] in nomor3 else "Tidak valid"
    print(f"\nData {i + 1}:")
    print(f"Sebelum : {nomorasli[i]}")
    print(f"Sesudah : {nomor2[i]}")
    print(f"Status  : {status}")

print(f"\nJumlah nomor valid: {len(nomor3)}")

"""
dibawah hanya prototypr awal
"""
# nomor2 = []
# angka_awal = 1
# while True:
   
#     try:
#         if jumlahdata > 0:
#             nomor1 = int(input(f"Nomor ke-{angka_awal}:"))
#             nomor3 = str(nomor1)
#             nomor2.append(nomor3)
#             angka_awal += 1
#             jumlahdata -= 1
#             continue
#         elif jumlahdata == 0 :
#             break
#     except ValueError: 
#         print("Input harus berupa angka!")
#         continue
