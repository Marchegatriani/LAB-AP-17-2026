import os
import random
from datetime import datetime

# Pastikan folder 'invoices' ada untuk menyimpan file teks invoice
if not os.path.exists("invoices"):
  os.makedirs("invoices")


def buat_transaksi():
  print("\n=== BUAT INVOICE / TRANSAKSI BARU ===")
  nama_kasir = input("Masukkan nama kasir: ").strip()
  if not nama_kasir:
    print("Nama kasir tidak boleh kosong!")
    return

  # Mengambil inisial nama kasir dalam huruf kapital (contoh: "Kiki Lestari" -> "KL")
  inisial_kasir = "".join([kata[0].upper() for kata in nama_kasir.split()])

  items = []
  while True:
    nama_produk = input(
        "Masukkan nama produk (ketik 'selesai' jika sudah cukup): "
    )
    if nama_produk.lower() == "selesai":
      break
    try:
      harga_produk = float(input("Masukkan harga produk: "))
      jumlah_produk = int(input("Masukkan jumlah produk: "))
      subtotal = harga_produk * jumlah_produk
      items.append(
          {
              "nama": nama_produk,
              "harga": harga_produk,
              "jumlah": jumlah_produk,
              "subtotal": subtotal,
          }
      )
    except ValueError:
      print("Harga harus berupa angka dan jumlah harus berupa bilangan bulat!")

  if not items:
    print("Transaksi dibatalkan karena tidak ada produk yang dimasukkan.")
    return

  # Mengambil komponen waktu saat ini
  waktu_sekarang = datetime.now()
  rand_num = random.randint(100, 999)  # Tiga digit angka acak (100-999)

  # Format ID Transaksi sesuai ketentuan
  id_transaksi = f"{inisial_kasir}{waktu_sekarang.strftime("%y%m%d%H%M")}{rand_num}"
  filename = f"invoices/{id_transaksi}.txt"

  # Menghitung total transaksi
  total_transaksi = sum(item["subtotal"] for item in items)

  # Membuat isi teks invoice
  invoice_content = f"""========================================
             STRUK BELANJA / INVOICE
========================================
ID Transaksi : {id_transaksi}
Waktu        : {waktu_sekarang.strftime('%Y-%m-%d %H:%M:%S')}
Kasir        : {nama_kasir}
----------------------------------------
Daftar Belanja:
"""
  for item in items:
    invoice_content += f"- {item['nama']} ({item['jumlah']}x @ Rp{item['harga']:,.0f}) = Rp{item['subtotal']:,.0f}\n"

  invoice_content += f"""----------------------------------------
Total Pembayaran: Rp{total_transaksi:,.0f}
========================================
Terima kasih telah berbelanja!
"""

  # Menyimpan invoice ke dalam folder 'invoices'
  with open(filename, "w", encoding="utf-8") as f:
    f.write(invoice_content)

  # Mencatat ke file riwayat transaksi (trx_history.txt)
  history_file = "trx_history.txt"
  file_exists = os.path.exists(history_file)

  with open(history_file, "a", encoding="utf-8") as f:
    if not file_exists:
      # Membuat header tabel jika file riwayat belum ada
      f.write(
          "+---------------------+-------------------+-------------------+\n"
      )
      f.write(
          "|        Waktu        |   ID Transaksi    | Nominal Transaksi |\n"
      )
      f.write(
          "+---------------------+-------------------+-------------------+\n"
      )

    waktu_str = waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")
    nominal_str = f"Rp. {total_transaksi:,.0f}"
    f.write(
        f"| {waktu_str:<19} | {id_transaksi:<17} | {nominal_str:<17} |\n"
    )
    f.write(
        "+---------------------+-------------------+-------------------+\n"
    )

  print(
      f"\n[SUKSES] Transaksi berhasil! ID Transaksi Anda: {id_transaksi}"
  )


def cari_invoice():
  print("\n=== CARI & TAMPILKAN INVOICE ===")
  id_cari = input("Masukkan ID Transaksi (contoh: KLS2308291250123): ").strip()
  filename = f"invoices/{id_cari}.txt"

  if os.path.exists(filename):
    print(f"\n--- Hasil Pencarian Invoice: {id_cari} ---")
    with open(filename, "r", encoding="utf-8") as f:
      print(f.read())
  else:
    print(f"Maaf, invoice dengan ID '{id_cari}' tidak ditemukan.")


def lihat_riwayat():
  print("\n=== RIWAYAT TRANSAKSI (TRX HISTORY) ===")
  history_file = "trx_history.txt"
  if os.path.exists(history_file):
    with open(history_file, "r", encoding="utf-8") as f:
      print(f.read())
  else:
    print("Belum ada riwayat transaksi yang tercatat.")


def main():
  while True:
    print("\n===============================")
    print("   APLIKASI KASIR SEDERHANA    ")
    print("===============================")
    print("1. Buat Transaksi / Invoice Baru")
    print("2. Cari & Tampilkan Invoice")
    print("3. Lihat Riwayat Transaksi")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ").strip()
    if pilihan == "1":
      buat_transaksi()
    elif pilihan == "2":
      cari_invoice()
    elif pilihan == "3":
      lihat_riwayat()
    elif pilihan == "4":
      print("Keluar dari aplikasi. Terima kasih!")
      break
    else:
      print("Pilihan tidak valid, silakan masukkan angka 1 sampai 4.")


if __name__ == "__main__":
  main()