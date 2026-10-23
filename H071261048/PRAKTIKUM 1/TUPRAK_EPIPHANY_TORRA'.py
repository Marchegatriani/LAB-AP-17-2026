menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah =[4, 3, 5]

sub_kopi = harga[0]*jumlah[0]
sub_matcha = harga[1]*jumlah[1]
sub_americano = harga[2]*jumlah[2]

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

BIAYA_OPERASIONAL = 15000
total_keseluruhan = sub_kopi+sub_matcha+sub_americano
pendapatan_bersih = total_keseluruhan - BIAYA_OPERASIONAL

jumlah_barang_terjual = jumlah[0]+jumlah[1]+jumlah[2]
target_tercapai = total_keseluruhan > 200000 and jumlah_barang_terjual > 10

print ("~~Laporan Penjualan 'Kopi Senja'~~")
print ("subtotal pendapatan:", subtotal_pendapatan)
print ("pendapatan bersih:", pendapatan_bersih)
print ("target yang tercapai:", target_tercapai)