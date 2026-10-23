ALFABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cek_kata(teks, kata):
    indeks = []
    start = 0 

    teks_kecil = teks.lower()
    kata_kecil = kata.lower()

    while True:
        posisi = teks_kecil.find(kata_kecil, start)

        if posisi == -1:
            break

        indeks.append(posisi)
        start = posisi + 1

    return indeks

def cek_batas_kata(teks, indeks, panjang_kata):
    if indeks == 0:
        batas_kiri = True
    else:
        karakter_sebelum = teks[indeks - 1]
        batas_kiri = karakter_sebelum not in ALFABET

    posisi_akhir = indeks + panjang_kata

    if posisi_akhir == len(teks):
        batas_kanan = True
    else:
        karakter_setelah = teks[posisi_akhir]
        batas_kanan = karakter_setelah not in ALFABET

    return batas_kiri and batas_kanan
def sensor_kata(teks, kata, simbol):
    indeks_semua = cek_kata(teks, kata)

    hasil = ""
    jumlah_sensor = 0
    indeks_valid = []

    posisi_terakhir = 0 

    for indeks in indeks_semua:
        if cek_batas_kata(teks, indeks, len(kata)):
         hasil += teks[posisi_terakhir:indeks]
        hasil += simbol * len(kata)
        posisi_terakhir = indeks + len(kata)
        jumlah_sensor += 1
        indeks_valid.append(indeks)

hasil += teks[posisi_terakhir:]

return hasil, jumlah_sensor, indeks_valid

teks = input("Masukkan Teks:")
kata = input("Masukkan Kata Target: ")
simbol = input("Masukkan Simbol: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Tes indeks:", cek_kata(teks, kata))
print("Tes batas:", [cek_batas_kata(teks, i, len(kata))
                      for i in cek_kata(teks, kata)])

print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "Indeks:", indeks)
