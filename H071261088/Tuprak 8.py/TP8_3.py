#3. Pembersihan Data Nomor Telepon 
import re

def bersihkan_nomor(nomor):
    return re.sub(r"[^0-9]", "", nomor)

def validasi_nomor(nomor_bersih):
    pola = r"^[08][\d]{9,12}$"
    hasil = re.match(pola, nomor_bersih)
    return hasil is not None

def main():
    print("=== Pembersihan Data Nomor Telepon ===")
    print()
    
    while True:
        try: 
            jumlah_data = int(input("Masukkan jumlah data: ").strip())
            print()
            
            if jumlah_data <= 0:
                print("Jumlah harus lebih dari 0!")
                continue

            break

        except ValueError:
            print("Inputan harus berupa angka bulat!")
            print()

    list_sebelum = []
    list_sesudah = []
    list_status = []
    list_nomor_valid = []

    no_input = 1
    while no_input <= jumlah_data:
        nomor_mentah = input("Nomor ke-" + str(no_input) + ": ").strip()
        
        nomor_bersih = bersihkan_nomor(nomor_mentah)
        list_sebelum.append(nomor_mentah)
        list_sesudah.append(nomor_bersih)
        
        if validasi_nomor(nomor_bersih):
            list_status.append("Valid")
            list_nomor_valid.append(nomor_bersih)
        else:
            list_status.append("Tidak valid")
            
        no_input = no_input + 1
        
    print()
    print("--- Hasil Pembersihan ---")
    print()
    
    no_cetak = 1
    for i in range(jumlah_data):
        print("Data " + str(no_cetak) + ":")
        print("Sebelum : " + list_sebelum[i])
        print("Sesudah : " + list_sesudah[i])
        print("Status  : " + list_status[i])
        print()
        no_cetak = no_cetak + 1
        
    print("Jumlah nomor valid:", len(list_nomor_valid))

main()