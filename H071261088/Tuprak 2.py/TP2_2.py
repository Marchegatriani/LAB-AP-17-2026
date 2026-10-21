jarak = int(input("Masukkan jarak (km): "))
layanan_express = input("layanan express (ya/tidak): ")

if jarak < 5:
    tarif = 10000
elif 5 <= jarak <= 20:
    tarif = 20000
else:
    tarif = 35000

express = 15000 if layanan_express == "ya" else 0
total = tarif + express
print(f"Total tarif pengiriman: Rp{total}")