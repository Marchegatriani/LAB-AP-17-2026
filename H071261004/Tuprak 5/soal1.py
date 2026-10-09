ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""

    for karakter in teks: 
        if karakter.lower() in ALFABET:
            hasil += karakter.lower()

    return hasil 

def cek_palindrome(teks):
    balik = "".join(reversed(teks))

    if teks == balik:
        return True, -1

    for i in range(len(teks)):
        if teks[i] != balik[i]:
            return False, i
    return False, i

def inti_palindrome(teks):
    terbaik = ""
    indeks_terbaik = 0

    for i in range(len(teks)):
        for j in range(i + 1, len(teks) + 1):

            substring = teks[i:j]

            hasil_cek, indeks_beda = cek_palindrome(substring)

            if hasil_cek: 
                if len(substring) > len (terbaik):
                    terbaik = substring
                    indeks_terbaik = i

    return {"teks": terbaik, "panjang": len(terbaik), "indeks_awal": indeks_terbaik}

teks = input("Masukkan teks: ")
teks_bersih = bersihkan_teks(teks)
print("Teks Bersih:", teks_bersih)

hasil = inti_palindrome(teks_bersih)

print("Output Terharap: ", hasil)
