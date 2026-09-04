print("=== KALKULATOR TARIK TAKSI ONLINE ===")
tarif_dasar = 15000
tarif_per_km = 4500
jarak_km = int(input("Masukan jarak tempuh (dalam km): "))
total_bayar = tarif_dasar + (tarif_per_km * jarak_km)
print("total bayar taksi anda adalah : Rp", total_bayar)
