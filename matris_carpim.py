def carp(matris1, matris2):

    matris3 = [[sum(a * b for a, b in zip(matris1_row, matris2_col)) for matris2_col in zip(*matris2)] for matris1_row in matris1]
    return matris3

m_bir_sat = int(input("Birinci matrisin satir sayisini giriniz: "))
m_bir_sut = int(input("Birinci matrisin sutun sayisini giriniz: "))

m_iki_sat = int(input("İkinci matrisin satir sayisini giriniz: "))
m_iki_sut = int(input("İkinci matrisin sutun sayisini giriniz: "))

if m_bir_sut == m_iki_sat:

    matris1=[]
    matris2=[]

    for i in range(m_bir_sat):
        matris1 += [[0] *m_bir_sut]

    for i in range(m_bir_sat):
        for j in range(m_bir_sut):
            sayi = int(input("Birinci matrisin {}.satir {}.sutun elemanini giriniz: ".format(i+1, j+1)))
            matris1[i][j] = sayi

    for i in range(m_iki_sat):
        matris2 += [[0] *m_iki_sut]

    for i in range(m_iki_sat):
        for j in range(m_iki_sut):
            sayi = int(input("İkinci matrisin {}.satir {}.sutun elemanini giriniz: ".format(i+1, j+1)))
            matris2[i][j] = sayi

    sonuc = carp(matris1, matris2)

    print(sonuc)

else:
    print("Birinci matrisin sutun sayisi ile"
          "Ikinci matrisin satir sayisi aynı olmalı.")

