ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata):
    daftar_indeks = []
    if kata == "":
        return daftar_indeks
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    start = 0
    posisi = teks_kecil.find(kata_kecil, start)
    while posisi != -1:
        daftar_indeks.append(posisi)
        start = posisi + 1
        posisi = teks_kecil.find(kata_kecil, start)
    return daftar_indeks


def cek_batas_kata(teks, i, panjang):
    if i > 0 and teks[i - 1].lower() in ALFABET:
        return False
    akhir = i + panjang
    if akhir < len(teks) and teks[akhir].lower() in ALFABET:
        return False
    return True


def sensor_kata(teks, kata, simbol):
    semua_indeks = cek_kata(teks, kata)
    indeks_sensor = []
    for i in semua_indeks:
        if cek_batas_kata(teks, i, len(kata)):
            indeks_sensor.append(i)

    hasil = ""
    awal = 0
    for i in indeks_sensor:
        hasil = hasil + teks[awal:i] + simbol * len(kata)
        awal = i + len(kata)
    hasil = hasil + teks[awal:]

    return (hasil, len(indeks_sensor), indeks_sensor)


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")
if simbol == "":
    simbol = "*"
simbol = simbol[0]

teks_tersensor, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Hasil Teks:", teks_tersensor)
print("Jumlah:", jumlah, "| Indeks:", indeks)