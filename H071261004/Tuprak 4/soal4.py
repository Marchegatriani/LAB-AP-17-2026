def konversi_suhu(suhu, skala_asal, skala_tujuan):
    skala_asal = skala_asal.upper()
    skala_tujuan = skala_tujuan.upper()

    skala_valid = ["C", "F", "K"]

    if skala_asal not in skala_valid or skala_tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")

    if skala_asal == "C":
        celsius = suhu

    elif skala_asal == "F":
        celsius = (suhu - 32) * 5 / 9

    elif skala_asal == "K":
        celsius = suhu - 273.15

    if skala_tujuan == "C":
        hasil = celsius
    elif skala_tujuan == "F":
        hasil = (celsius * 9 / 5 + 32)
    elif skala_tujuan == "K":
        hasil = celsius + 273.15

    return hasil 

print("=== Konversi Suhu ===")

while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if input_suhu.lower() == "selesai":
        break
    try:
        suhu = float(input_suhu)
        input_skala_asal = input("Masukkan skala suhu asal (C/F/K): ")
        input_skala_tujuan = input("Masukkan skala suhu tujuan (C/F/K): ")

        hasil = konversi_suhu(suhu, input_skala_asal, input_skala_tujuan)
        print(f"Hasil : {hasil:.1f} {input_skala_tujuan.upper()}")
    except ValueError as e:
        print(f"Error: {e}")