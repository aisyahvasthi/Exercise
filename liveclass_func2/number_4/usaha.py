#modul usaha

#fungsi beban_usaha
def beban_usaha(beban_operasional, beban_non_operasional ):
    beban = beban_operasional + beban_non_operasional
    print(f'Beban usaha yang dikeluarkan sebesar : {beban}')
    return beban

#fungsi laba_bersih
def laba_bersih(biaya_operasional, biaya_non_operasional, beban_usaha):
    laba_bersih_v = (biaya_operasional + biaya_non_operasional) - beban_usaha
    print(f'Laba bersih yang dihasilkan sebesar : {laba_bersih_v}')
    return laba_bersih_v