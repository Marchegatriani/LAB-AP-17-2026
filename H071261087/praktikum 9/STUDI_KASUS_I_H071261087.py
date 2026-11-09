# class Pemain:
#     def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
#         self.nama = nama
#         self.id_pemain = id_pemain
#         self.role = role
#         self.nilai_kill = nilai_kill
#         self.nilai_assist = nilai_assist
#         self.nilai_objective = nilai_objective

#     def hitung_skor_akhir(self):
#         skor_akhir = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
#         return skor_akhir

#     def status_performa(self):
#         if self.hitung_skor_akhir() >= 60:
#             return "Unggul"
#         else:
#             return "Perlu Evaluasi"

#     def tampilkan_data(self):
#         print(f"| {self.nama:<10} | {self.id_pemain:<10} | {self.role:<10} | {self.hitung_skor_akhir():<10} | {self.status_performa():<10} |")

# print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
# daftar_pemain = []
# jumlah = int(input("Masukkan jumlah pemain: "))

# for i in range(jumlah):
#     print(f"\n-- Data Pemain ke-{i + 1} --")
#     nama = input("Nama pemain: ")
#     id_pemain = input("ID pemain: ")
#     role = input("Role pemain: ")
#     nilai_kill = int(input("Nilai Kill: "))
#     nilai_assist = int(input("Nilai Assist: "))
#     nilai_objective = int(input("Nilai Objective: "))

#     pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist,nilai_objective)
#     daftar_pemain.append(pemain)

# print("\n=== REKAPITULASI PEFORMA PEMAIN ===")
# print("=" * 71)
# print(f"| {"No"} | {'Nama':<10} | {'ID Pemain':<10} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<10} |")
# print("=" * 71)

# for i, pemain in enumerate(daftar_pemain):
#     print(f"{i+1:<5}", end="")
#     pemain.tampilkan_data()
# print("=" * 71)

# =======================================================================================================================================================================================

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
        if self.hitung_skor_akhir() >= 70: 
            return "Platinum"
        if self.hitung_skor_akhir() >= 60: 
            return "Gold"
        else:
            return "Bronze"

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self):
        print(f"| {self.nama:<10} | {self.id_pemain:<10} | {self.role:<10} | {self.hitung_skor_akhir():<10} | {self.status_performa():<10} | {self.tentukan_level():<10} |")

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
daftar_pemain = []
jumlah = int(input("Masukkan jumlah pemain: "))

for i in range(jumlah):
    print(f"\n-- Data Pemain ke-{i + 1} --")
    nama = input("Nama pemain: ")
    id_pemain = input("ID pemain: ")
    role = input("Role pemain: ")
    nilai_kill = int(input("Nilai Kill: "))
    nilai_assist = int(input("Nilai Assist: "))
    nilai_objective = int(input("Nilai Objective: "))

    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist,nilai_objective)
    daftar_pemain.append(pemain)

print("\n=== REKAPITULASI PEFORMA PEMAIN ===")
print("=" * 71)
print(f"| {"No"} | {'Nama':<10} | {'ID Pemain':<10} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<10} | {'Level':<10} |")
print("=" * 71)

for i, pemain in enumerate(daftar_pemain):
    print(f"{i+1:<5}", end="")
    pemain.tampilkan_data()
print("=" * 71)

print("\n===PENCARIAN PEMAIN===")

inputID = input("\nMasukkan ID Pemain : ")

valid =  False

for pemain in daftar_pemain:
    if pemain.id_pemain == inputID:
        print(("Nama").ljust(12) + f": {pemain.nama}")
        print(("ID").ljust(12) + f": {pemain.id_pemain}")
        print(("Role").ljust(12) + f": {pemain.role}")
        print(("Skor Akhir").ljust(12) + f": {pemain.hitung_skor_akhir()}")
        print(("Peforma").ljust(12) + f": {pemain.status_performa()}")
        valid = True
        break

if not valid:
    print("Pemain tidak ditemukan!")