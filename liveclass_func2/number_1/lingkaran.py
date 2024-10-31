from math import pi

def luas_lingkaran():
    jari_jari_lingkaran = float(input("Masukkan jari-jari lingkaran: "))
    rumus_luas_lingkaran = pi * jari_jari_lingkaran * jari_jari_lingkaran
    #hasil_luas = print(f'Luas Lingkaran adalah {rumus_luas_lingkaran}')
    return rumus_luas_lingkaran

def keliling_lingkaran():
    jari_jari_lingkaran = float(input("Masukkan jari-jari lingkaran: "))
    rumus_kel_lingkaran = 2 * pi * jari_jari_lingkaran
    #hasil_keliling = print(f'Hasil keliling lingkaran adalah {rumus_kel_lingkaran}')
    return rumus_kel_lingkaran