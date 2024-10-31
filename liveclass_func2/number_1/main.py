import lingkaran 
import persegi_panjang
import segitiga

bangun_ruang = input("Bangun ruang apa yang ingin anda Hitung (lingkaran/persegi panjang/segitiga): ")
l_or_k = input("Apa yang ingin anda hitung (luas/keliling): ")
if bangun_ruang == 'lingkaran':
    if l_or_k == 'luas':
        luas = lingkaran.luas_lingkaran()
        print(luas)

    else:
        keliling = lingkaran.keliling_lingkaran()
        print(keliling)

elif bangun_ruang == 'persegi panjang':
    if l_or_k == 'luas':
        luas = persegi_panjang.luas_persegi_panjang()
        print(luas)

    else:
        keliling = persegi_panjang.keliling_persegi_panjang()
        print(keliling)

elif bangun_ruang == 'segitiga':
    if l_or_k == 'luas':
        luas = segitiga.luas_segitiga()
        print(luas)

    else:
        keliling = segitiga.keliling_segitiga()
        print(keliling)

else:
    print("Tidak termasuk dalam pilihan")



