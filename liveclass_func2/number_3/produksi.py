#modul produksi
#fungsi keuntungan penjualan
def profit(data):
    untung = (data['jumlah_produk'] * data['harga_jual']) - (data['jumlah_produk'] * data['biaya_produksi'])
    print(f'Profit yang didapat bulan ini adalah : Rp {untung}')
    return untung


#fungsi harga pokok penjualan
def harga_pokok_penjualan(data):
    harga_pokok = data['biaya_produksi'] + data['jumlah_produk'] - data['persediaan_sisa']
    print(f'Harga pokok yang dikeluarkan adalah : Rp {harga_pokok}')
    return harga_pokok
