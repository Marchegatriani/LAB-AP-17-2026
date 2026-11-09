import os
import random
from datetime import datetime

FOLDER_INVOICE = "invoices"
FILE_RIWAYAT = "trx_history.txt"

# Soal 1
def buat_id_transaksi(kasir, waktu):
    """Format: inisial + yy + mm + dd + HHMM + 3 digit acak."""
    inisial = "".join(kata[0] for kata in kasir.split()).upper()
    bagian_waktu = waktu.strftime("%y%m%d%H%M")
    while True:
        id_trx = f"{inisial}{bagian_waktu}{random.randint(100, 999)}"
        if not os.path.exists(os.path.join(FOLDER_INVOICE, id_trx + ".txt")):
            return id_trx


def buat_isi_invoice(id_trx, kasir, waktu, items, total):
    garis = "=" * 47
    baris = [
        garis,
        "INVOICE PEMBELIAN".center(47),
        garis,
        f"ID Transaksi : {id_trx}",
        f"Waktu        : {waktu:%Y-%m-%d %H:%M:%S}",
        f"Kasir        : {kasir}",
        "-" * 47,
        f"{'No':<4}{'Produk':<16}{'Harga':>10}{'Jml':>5}{'Subtotal':>12}",
        "-" * 47,
    ]
    for no, (nama, harga, jumlah) in enumerate(items, 1):
        baris.append(f"{no:<4}{nama:<16}{harga:>10}{jumlah:>5}{harga * jumlah:>12}")
    baris += ["-" * 47, f"{'TOTAL':<35}{'Rp. ' + str(total):>12}", garis]
    return "\n".join(baris) + "\n"


def simpan_invoice(id_trx, isi):
    os.makedirs(FOLDER_INVOICE, exist_ok=True)
    path = os.path.join(FOLDER_INVOICE, id_trx + ".txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(isi)
    return path

# Soal 3: Riwayat
def catat_riwayat(waktu, id_trx, total):
    garis = "=" * 66
    baru = not os.path.exists(FILE_RIWAYAT) or os.path.getsize(FILE_RIWAYAT) == 0
    with open(FILE_RIWAYAT, "a", encoding="utf-8") as f:
        if baru:
            f.write(garis + "\n")
            f.write(f"| {'Waktu':<19} | {'ID Transaksi':<20} | {'Nominal Transaksi':<17} |\n")
            f.write(garis + "\n")
        f.write(f"| {waktu:%Y-%m-%d %H:%M:%S} | {id_trx:<20} | {'Rp. ' + str(total):<17} |\n")
        f.write(garis + "\n")


def lihat_riwayat():
    if not os.path.exists(FILE_RIWAYAT):
        print("Belum ada riwayat transaksi.")
        return
    with open(FILE_RIWAYAT, "r", encoding="utf-8") as f:
        print(f.read())


# Soal 2: mencari invoice

def cari_invoice(id_trx):
    id_trx = id_trx.strip().upper()
    if not id_trx.isalnum():
        print("ID transaksi tidak valid.")
        return
    path = os.path.join(FOLDER_INVOICE, id_trx + ".txt")
    if not os.path.exists(path):
        print(f"Invoice dengan ID '{id_trx}' tidak ditemukan.")
        return
    with open(path, "r", encoding="utf-8") as f:
        print(f.read())


def input_angka_positif(pesan):
    while True:
        try:
            angka = int(input(pesan))
            if angka <= 0:
                print("Harus lebih dari 0.")
                continue
            return angka
        except ValueError:
            print("Input harus berupa angka.")


def transaksi_baru():
    kasir = ""
    while kasir == "":
        kasir = input("Nama kasir: ").strip()

    items = []
    while True:
        nama = input("Nama produk (kosongkan jika selesai): ").strip()
        if nama == "":
            if not items:
                print("Minimal harus ada 1 produk.")
                continue
            break
        harga = input_angka_positif("Harga produk: ")
        jumlah = input_angka_positif("Jumlah dibeli: ")
        items.append((nama, harga, jumlah))

    waktu = datetime.now()
    total = sum(harga * jumlah for _, harga, jumlah in items)
    id_trx = buat_id_transaksi(kasir, waktu)
    isi = buat_isi_invoice(id_trx, kasir, waktu, items, total)

    simpan_invoice(id_trx, isi)
    catat_riwayat(waktu, id_trx, total)

    print("\nTransaksi berhasil!")
    print(f"Invoice disimpan: {FOLDER_INVOICE}/{id_trx}.txt\n")
    print(isi)


def main():
    print("=" * 40)
    print(" APLIKASI KASIR SEDERHANA")
    print("=" * 40)

    while True:
        print("Menu:")
        print("1. Transaksi Baru")
        print("2. Cari Invoice")
        print("3. Lihat Riwayat Transaksi")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            transaksi_baru()
        elif pilihan == "2":
            cari_invoice(input("Masukkan ID transaksi: "))
        elif pilihan == "3":
            lihat_riwayat()
        elif pilihan == "4":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Pilih 1-4.")


if __name__ == "__main__":
    main()