import re

class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective
    

    def hitung_skor_akhir(self):
        skor_akhir = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor_akhir

    def tentukan_level(self):
        if self.hitung_skor_akhir() >= 85:
            return "Diamond"
        elif self.hitung_skor_akhir() >= 70:
            return "Platinum"
        elif self.hitung_skor_akhir() >= 60:
            return "Gold"
        else:
            return "Bronze"
        
    def status_performa(self):
        skor = self.hitung_skor_akhir()
        if skor >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"
        


    def tampilkan_data(self, no):
        print(f"| {no:<2} | {self.nama:<10} | {self.id_pemain:<10} | {self.role:<10} | "
              f"{self.hitung_skor_akhir():<10.2f} | {self.status_performa():<14} | {self.tentukan_level():<14}")
        

def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks != "":
            return teks
        print("Input tidak boleh kosong!")


def input_angka(pesan, minimal, maksimal):
    while True:
        try:
            angka = int(input(pesan))
            if minimal <= angka <= maksimal:
                return angka
            print(f"Angka harus antara {minimal} sampai {maksimal}!")
        except ValueError:
            print("Input harus berupa angka bulat!")


def input_id(pesan):
    while True:
        id_pemain = input(pesan).strip().upper()
        if re.fullmatch(r"P07\d{7}", id_pemain):
            return id_pemain
        print("ID tidak valid! Harus diawali P07 diikuti 7 angka (contoh: P071261001).")


def input_role(pesan):
    daftar_role = ["Tank", "Fighter", "Assassin", "Mage", "Marksman", "Support"]
    while True:
        role = input(pesan).strip().title()
        if role in daftar_role:
            return role
        print("Role tidak valid! Pilihan: Tank, Fighter, Assassin, Mage, Marksman, Support.")



print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===\n")
daftar_pemain = []
jumlah = input_angka("Masukkan jumlah pemain: ", 1, 100)

for i in range(1, jumlah + 1):
    print(f"\n-- Data Pemain ke-{i} --")
    nama = input_teks("Nama: ")
    id_pemain = input_id("ID Pemain: ")
    role = input_role("Role: ")
    nilai_kill = input_angka("Nilai Kill: ", 0, 100)
    nilai_assist = input_angka("Nilai Assist: ", 0, 100)
    nilai_objective = input_angka("Nilai Objective: ", 0, 100)
    
    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
    daftar_pemain.append(pemain)

garis = "=" * 76
print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print(garis)
print(f"| {'No':<2} | {'Nama':<10} | {'ID Pemain':<10} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<14} | {'Level':<10}")
print(garis)

nomor = 1
for pemain in daftar_pemain:
    pemain.tampilkan_data(nomor)
    nomor += 1
print(garis)

print("=== PENCARIAN PEMAIN ===")
inputid = input("Masukkan ID Pemain: ", ).strip().upper()

for pemain in daftar_pemain:
    if pemain.id_pemain == inputid:
        print(f"nama : {pemain.nama}\nID : {pemain.id_pemain}\nRole : {pemain.role}\nSkor Akhir : {pemain.hitung_skor_akhir()}\nStatus : {pemain.status_performa()}")
        break
    else:
        print("Pemain tidak ditemukan!")

