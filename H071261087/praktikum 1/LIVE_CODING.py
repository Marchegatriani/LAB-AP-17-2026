# data awal
menu  = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [1, 1, 1]

# main subtotal

subtotal_kopi = harga[0] * jumlah[0]
subtotal_matcha = harga[1] * jumlah[1]
subtotal_americano = harga[2] * jumlah[2]

subtotal_pendapatan = [subtotal_kopi, subtotal_matcha, subtotal_americano]

# main di total

total_seluruh = subtotal_kopi + subtotal_matcha + subtotal_americano
biaya_operasional = 15000
pendapatan_bersih = [total_seluruh - biaya_operasional]

total_jumlah = jumlah[0] + jumlah[1] + jumlah[2]

target_tercapai = total_seluruh > 200000 or total_jumlah > 10

# print pritn momen

print("target tercapai :", target_tercapai)