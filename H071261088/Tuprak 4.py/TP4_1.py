def sistem(harga, jumlah, adalah_member=False):
    harga_jumlah = harga * jumlah

    if adalah_member:
        harga_jumlah = harga_jumlah * 0.9 #(1 - 0.1) atau 90/100
    
    return int(harga_jumlah)

print("Selamat datang di kasir Minimarket!")

total_belanja = 0
while True:
    status_member = input("Apakah Anda member? (y/n): ")
    if status_member == "y":
        member = True
        break
    elif status_member == "n":
        member = False
        break
    else:
        print("Input yang anda masukkan tidak valid")
        continue

while True:
    try:
        nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
        if nama_barang == "":
            print(f"Total belanja: {total_belanja}")
            break
        
        harga_barang = int(input("Harga barang: "))
        if harga_barang < 0:
            raise ValueError
        
        jumlah_barang = int(input("Jumlah barang: "))
        if jumlah_barang <= 0:
            raise ValueError 
        
        subtotal = sistem(harga_barang, jumlah_barang, member)

        total_belanja += subtotal
        print(f"Subtotal {nama_barang}: {subtotal}")
        
    except ValueError:
        print("Input yang anda masukkan tidak valid")