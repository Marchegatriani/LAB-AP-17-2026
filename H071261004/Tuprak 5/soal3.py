ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):

    if ch in ALFABET: 
        posisi = ALFABET.find(ch)
        posisi_baru = (posisi + k) % 26
        return ALFABET[posisi_baru]

    huruf_kecil = ch.upper()

    if huruf_kecil in ALFABET:
        posisi = ALFABET.find(huruf_kecil)
        posisi_baru = (posisi + k) % 26
        return ALFABET[posisi_baru].upper()
    
    return ch

def mesin_deskripsi(teks, k):
 return mesin_deskripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        pesan_asli = mesin_deskripsi(sandi, k)
        if pesan_asli.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan_asli))
            return hasil

sandi = input("Masukkan pesan tersita (enskripsi ceasar): ")
kata_kunci = input("Masukkan kata kunci target:")

hasil = retas_sandi(sandi, kata_kunci)

print("Output deskripsi:", hasil)