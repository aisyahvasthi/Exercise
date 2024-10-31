#import bunga_bank
import konversi_hari
import konversi_jam
import konversi_menit

#from bunga_bank import * # * adalah untuk memanggil semua fungsi yg ada didalam modul
#rendah_1 = bunga_terendah(2000000, 10)
#anuitas_2 = bunga_anuitas(700000, 8)

#print(f"Bunga terendah yang didapatkan adalah Rp {rendah_1}")
#print(f"Bunga anuitas yang didapatkan adalah Rp {anuitas_2}")

#hari_jam = konversi_hari.jam(1)
#hari_menit = konversi_hari.menit(1)
#hari_detik = konversi_hari.detik(1)

#hari_hari = konversi_jam.hari(1)
#hari_menit = konversi_jam.menit(1)
#hari_detik = konversi_jam.detik(1)

#hari_hari = konversi_menit.hari(1)
#hari_jam = konversi_menit.jam(1)
#hari_detik = konversi_menit.detik(1)
0
from Test_folder.perhitungan_penjualan import profit as penjualan

#dapat_laba = laba_bersih(50000, 35000)
jumlah_profit = penjualan(150, 35000,30000)
#print(f'Pendapatan laba bersih adalah {dapet_laba}')
print(f'Total profit adalah adalah {jumlah_profit}')