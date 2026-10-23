ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks): 
    hasil = ""
    for karakter in teks: 
        if karakter.lower() in ALFABET: 
            hasil = hasil + karakter.lower() 
    return hasil

def cek_palinrome(teks):
    teks_terbalik = "".join(reversed(teks))
    panjang_teks = len(teks)
    for i in range(panjang_teks):
        if teks[i] != teks_terbalik[i]:
            return (False, i) 
    return (True, -1) 

def inti_palinrome(teks):
    terbaik = {"teks": "", 
               "panjang": 0, 
               "indeks_awal": -1}
    n = len(teks)
    
    for i in range(n):
        for j in range(i + 1, n + 1): 
            potongan = teks[i:j]
            if cek_palinrome(potongan)[0]: 
                if len(potongan) > terbaik["panjang"]:
                    terbaik = {"teks": potongan,
                                "panjang": len(potongan),
                                "indeks_awal": i}
    return terbaik
    
teks = input("Masukkan teks prasasti: ")
bersih = bersihkan_teks(teks)
print()
print("Teks Bersih:", bersih)
print("Output Terharap:", inti_palinrome(bersih)) 