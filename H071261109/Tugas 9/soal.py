class Pemain:
    def __init__(self, nama, ID_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.ID_pemain = ID_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_score(self):
        score = (self.nilai_kill * 0.3) + (self.nilai_assist * 0.3) + (self.nilai_objective * 0.4)
        return score

    def status_performa(self):
        if self.hitung_score () >= 60 :
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tentukan_level(self):
        if self.hitung_score()  >= 80:
            return "Diamond"
        elif self.hitung_score() >= 60:
            return "Gold"
        elif self.hitung_score() >= 70:
            return "Platinum"
        else:
            return "Bronze"

    def tampilkan_data(self):
        print(f"|{i:<2}|{self.nama:<13} | {self.ID_pemain:<10} | {self.role:<10} | {self.nilai_kill:<12} | {self.nilai_assist:<14} | {self.nilai_objective:<17} | {self.hitung_score():<5.2f} | {self.status_performa():<15} | {self.tentukan_level():10}")

print(f"=== SISTEM PENILAIAN PERFORMA PEMAIN === \n")

pemain_list = []

while True:
    try:
        jumlah_pemain = int(input("Masukkan jumlah pemain:"))
        if jumlah_pemain <= 0:
            print("Jumlah pemain harus lebih dari 0. Silakan coba lagi.")
            continue
        break
    except ValueError:
        print("Input tidak valid")

for i in range(jumlah_pemain):
    print(f"-- Data Pemain ke-{i+1} --")
    nama = input(f"Nama: ")
    ID_pemain = input(f"ID Pemain: ")
    role = input(f"Role: ")

    while True:
        try:
            nilai_kill = int(input("Nilai Kill: "))
            nilai_assist = int(input("Nilai Assist: "))
            nilai_objective = int(input("Nilai Objective: "))
            if  0 < nilai_kill <100 and 0 < nilai_assist <100 and 0 < nilai_objective <100:
                break
            else:
                print("Nilai harus diantara 0-100")
        except ValueError:
            print("Input tidak valid")

    pemain = Pemain(nama, ID_pemain, role, nilai_kill, nilai_assist, nilai_objective)
    pemain_list.append(pemain)

print(f"=== REKAPITULASI PERFORMA PEMAIN ===")
print("="*123)
print(f"|No|    Nama      | ID Pemain  |    Role    |  Nilai Kill  |  Nilai Assist  |  Nilai Objective  | Score | Status Performa |  Level   |")
print("="*123)

for i, pemain in enumerate(pemain_list, start=1):
    pemain.tampilkan_data()
    
print("="*123)



valid = False
ID_pemain = input("ID_pemain: ")
for pemain in pemain_list:
    if pemain.ID_pemain == ID_pemain:
        print(f" nama            : {pemain.nama}")
        print(f" id_pemain       : {pemain.ID_pemain}")
        print(f" role            : {pemain.role}")
        print(f" skor akhir      : {pemain.hitung_score()}")
        print(f" status performa : {pemain.status_performa()}")
        valid = True
        break

if not valid:
    print("Pemain tidak ditemukan!")