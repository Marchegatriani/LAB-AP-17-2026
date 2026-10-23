# tugas praktikum 1, usu kanda welllll

menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# sub total brok (intina di kali kali ki harga dan jumlah trus dijadikangi variabel baru cak wkwkwk)
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# total totalan cihuyyyyyy (main main di sum sum mi, kyk di excel anjayy sm buat lagi variabel untuk para kanda kanda total)
total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

total_barang = sum(jumlah)
target_tercapai = (total_seluruh > 200000) and (total_barang > 10)

# TIME TO SHINEEEEEEEEEEEEEEEEEE (PRINT SEMUAAAAAAAAAAAAA PRINTTTT + kasi rapi ki toh jg wkwkkw)
print("=== LAPORAN PENJUALAN KOPI SENJA ===")
print(f"List Subtotal       : {subtotal_pendapatan} ")
print(f"Pendapatan Bersih   : Rp{pendapatan_bersih:,}")
print(f"Target Tercapai?    : {target_tercapai}")