menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah =[4, 3, 5]

sub_kopi = harga[0]*jumlah[0]
sub_matcha = harga[1]*jumlah[1]
sub_americano = harga[2]*jumlah[2]

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

jumlah_barang = jumlah[0]+jumlah[1]+jumlah[2]

BIAYA_OPERASIONAL = 15000
subtotal_keseluruhan = sub_kopi+sub_matcha+sub_americano
pendapatan_bersih = subtotal_keseluruhan - BIAYA_OPERASIONAL
target_tercapai = subtotal_keseluruhan > 200000 and jumlah_barang > 10

print ("apakah target tercapai:", target_tercapai)
