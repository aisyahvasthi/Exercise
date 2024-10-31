import perhitungan_angsuran_per_bulan_klien as angsuran_per_bulan

angsuran = angsuran_per_bulan.bunga_flat(10000000, 10)
print(f'Angsuran perbulan yang wajib dibayar Rp. {round(angsuran)}')