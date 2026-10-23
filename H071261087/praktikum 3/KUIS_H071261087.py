print("SIMULASI SEGITIGA SAMA KAKI")
# Kesusahan karena memang di saya kesusahan di nested loop yang pakai for

jumlah_baris = int(input("Masukkan jumlah baris segitiga: "))

for i in range(1, jumlah_baris + 1):
    # Intinya sepahaman ku yang menyediakan baris untuk loop lainnya bisa kerjakan.

    for j in range(jumlah_baris - i):
        print(" ", end="")
    # yang buat spasinya diawal sampai akhir nya, semakin lama semakin berkurang.
    
    for k in range(2 * i - 1):
        print("*", end="")
    # membuat bintang-bintang nya jadi ganjil krn hal apapun klo di bagi dua trus dikurang 1, pasti ganjil.
    
    print()
    # yang ini sy kurang mengerti, bukannya "print()" gunanya untuk buat "enter" di hasil print nya nanti??