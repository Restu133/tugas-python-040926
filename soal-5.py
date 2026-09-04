print("=== KALKULATOR PATUNGAN (SPLIT BILL) ===")

# Mengambil input dari pengguna
tagihan_makanan = int(input("Masukkan total tagihan makanan: Rp "))
biaya_layanan = int(input("Masukkan biaya layanan: Rp "))
jumlah_orang = int(input("Masukkan jumlah orang: "))

# Proses hitung
bayar_per_orang = (tagihan_makanan + biaya_layanan) / jumlah_orang

# Menampilkan hasil
print("Uang patungan per orang adalah: Rp", bayar_per_orang)
