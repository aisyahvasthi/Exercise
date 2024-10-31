#modul perhitungan_angsuran_per_bulan_klien.py

#fungsi bunga anuitas
def bunga_anuitas(pinjaman, bunga):
    hari = 30
    tabungan = pinjaman * bunga * hari
    return tabungan

#fungsi bunga flat
def bunga_flat(pinjaman,bunga):
    bunga_per_tahun = pinjaman * 0.1
    bunga_per_bulan = bunga_per_tahun / 12
    pokok_pinjaman = pinjaman / 12
    angsuran_bunga_flat = pokok_pinjaman + bunga_per_bulan
    return angsuran_bunga_flat

