menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4,3,5]

sub_kopi = harga[0]*jumlah[0]
sub_matcha = harga[1]*jumlah[1]
sub_americano = harga[2]*jumlah[2]
print(sub_kopi)
print(sub_matcha)
print(sub_americano)

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]
total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL
print(pendapatan_bersih)

jumlah_barang = sum(jumlah)
target_tercapai = (total_seluruh > 200000) or (jumlah_barang > 10)
print(target_tercapai)