print("=== KALKULATOR KEBUTUHAN PAGAR KEBUN ===")

panjang = float(input("Masukkan panjang kebun (meter): "))
lebar = float(input("Masukkan lebar kebun (meter): "))

panjang_kawat = 2 * (panjang + lebar)

print("Panjang kawat yang dibutuhkan adalah:", panjang_kawat, "meter")
