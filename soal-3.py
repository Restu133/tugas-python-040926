print("=== KALKULATOR NILAI RAPORT ===")

nilai_tugas = float(input("Masukkan nilai Tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

nilai_rata_rata = (nilai_tugas + nilai_uts + nilai_uas) / 3

print("Nilai rata-rata siswa tersebut adalah:", nilai_rata_rata)
