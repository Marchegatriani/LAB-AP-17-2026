def hitung_subtotal(harga, jumlah, is_member=False):
    subtotal = harga * jumlah

    if is_member:
        subtotal = subtotal * 0.9 

        return int(subtotal)

print("Selamat datang di Kasir Minimarket!")

status_member = input("Apakah anda member? (y/n): ")

is_member = status_member.lower() == 'y'

total = 0

while True: 
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")

    if nama_barang == "":
        break 
    harga = int(input("Masukkan harga barang: "))
    jumlah = int(input("Masukkan jumlah barang:"))

    subtotal = hitung_subtotal(harga, jumlah, is_member)

    print(f"Subtotal untuk {nama_barang}: {subtotal}")

    total += subtotal 

    print(f"Total belanja: Rp{total}")
